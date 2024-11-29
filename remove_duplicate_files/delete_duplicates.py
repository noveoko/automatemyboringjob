from pathlib import Path
from collections import defaultdict
import asyncio
import aiofiles
import hashlib
from typing import Set, Dict, List, Optional
from dataclasses import dataclass, field
import logging
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.logging import RichHandler
import concurrent.futures

# Custom exceptions for better error handling
class DeduplicatorError(Exception):
    """Base exception for the deduplicator module"""
    pass

class FileAccessError(DeduplicatorError):
    """Raised when there are problems accessing files"""
    pass

class HashingError(DeduplicatorError):
    """Raised when there are problems computing file hashes"""
    pass

class InvalidPathError(DeduplicatorError):
    """Raised when a path is invalid or inaccessible"""
    pass

@dataclass
class FileInfo:
    """Stores information about a file including its hash and size"""
    path: Path
    hash: str
    size: int

@dataclass
class DedupStats:
    """Tracks statistics about the deduplication process"""
    files_processed: int = 0
    files_deleted: int = 0
    bytes_saved: int = 0
    unique_files: int = 0
    errors: int = 0
    
    def __str__(self) -> str:
        return (
            f"Files processed: {self.files_processed:,}\n"
            f"Duplicate files removed: {self.files_deleted:,}\n"
            f"Storage saved: {self.bytes_saved / (1024*1024*1024):.2f} GB\n"
            f"Unique files found: {self.unique_files:,}\n"
            f"Errors encountered: {self.errors}"
        )

class ModernDeduplicator:
    """
    A modern file deduplicator that uses async IO and parallel processing 
    to efficiently find and remove duplicate files.
    """
    
    def __init__(self, root_path: str | Path, chunk_size: int = 8192):
        self.root_path = Path(root_path)
        self.chunk_size = chunk_size
        self.stats = DedupStats()
        self._setup_logging()
        
        # Configure process pool for CPU-bound tasks
        self.process_pool = concurrent.futures.ProcessPoolExecutor()
        
    def _setup_logging(self):
        """Configure rich logging"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[RichHandler(rich_tracebacks=True)]
        )
        self.logger = logging.getLogger("deduplicator")

    async def compute_file_hash(self, path: Path) -> Optional[FileInfo]:
        """
        Compute a file's hash using xxhash (faster than md5/sha) and async IO
        """
        try:
            if not path.is_file():
                raise InvalidPathError(f"{path} is not a file")
                
            file_size = path.stat().st_size
            
            # Use asyncio's run_in_executor to run CPU-bound hashing in process pool
            async with aiofiles.open(path, 'rb') as f:
                hasher = hashlib.xxh64()
                while chunk := await f.read(self.chunk_size):
                    hasher.update(chunk)
                    
            return FileInfo(
                path=path,
                hash=hasher.hexdigest(),
                size=file_size
            )
            
        except (OSError, IOError) as e:
            self.stats.errors += 1
            self.logger.error(f"Error processing {path}: {str(e)}")
            raise FileAccessError(f"Cannot access {path}: {str(e)}")
        except Exception as e:
            self.stats.errors += 1
            self.logger.error(f"Unexpected error with {path}: {str(e)}")
            raise DeduplicatorError(f"Error processing {path}: {str(e)}")

    async def scan_directory(self) -> Dict[str, List[FileInfo]]:
        """
        Scan directory and group files by hash
        """
        duplicates: Dict[str, List[FileInfo]] = defaultdict(list)
        
        with Progress(
            SpinnerColumn(),
            *Progress.get_default_columns(),
            TimeElapsedColumn(),
        ) as progress:
            task = progress.add_task("[cyan]Scanning files...", total=None)
            
            async def process_file(path: Path):
                try:
                    file_info = await self.compute_file_hash(path)
                    if file_info:
                        duplicates[file_info.hash].append(file_info)
                        self.stats.files_processed += 1
                        progress.update(task, advance=1)
                except DeduplicatorError as e:
                    self.logger.warning(str(e))
                
            # Create tasks for all files
            tasks = []
            for path in self.root_path.rglob("*"):
                if path.is_file():
                    tasks.append(process_file(path))
            
            # Process files concurrently
            await asyncio.gather(*tasks)
            
        return duplicates

    def remove_duplicates(self, duplicates: Dict[str, List[FileInfo]], keep_newest: bool = True) -> None:
        """
        Remove duplicate files, keeping either the newest or oldest version
        """
        for hash_value, file_infos in duplicates.items():
            if len(file_infos) > 1:
                # Sort files by modification time
                sorted_files = sorted(
                    file_infos,
                    key=lambda x: x.path.stat().st_mtime,
                    reverse=keep_newest
                )
                
                # Keep the first file, delete the rest
                for file_info in sorted_files[1:]:
                    try:
                        file_info.path.unlink()
                        self.stats.files_deleted += 1
                        self.stats.bytes_saved += file_info.size
                        self.logger.info(f"Deleted duplicate: {file_info.path}")
                    except OSError as e:
                        self.stats.errors += 1
                        self.logger.error(f"Error deleting {file_info.path}: {str(e)}")

    async def deduplicate(self, keep_newest: bool = True) -> DedupStats:
        """
        Main method to run the deduplication process
        """
        self.logger.info(f"Starting deduplication in {self.root_path}")
        
        try:
            # Scan for duplicates
            duplicates = await self.scan_directory()
            
            # Update stats
            self.stats.unique_files = len(duplicates)
            
            # Remove duplicates
            self.remove_duplicates(duplicates, keep_newest)
            
            self.logger.info("Deduplication complete!")
            self.logger.info(str(self.stats))
            
            return self.stats
            
        except Exception as e:
            self.logger.error(f"Deduplication failed: {str(e)}")
            raise DeduplicatorError(f"Deduplication failed: {str(e)}")
        finally:
            self.process_pool.shutdown()

async def main():
    """
    Main entry point with example usage
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Modern file deduplicator")
    parser.add_argument("path", help="Root path to scan for duplicates")
    parser.add_argument(
        "--keep-oldest",
        action="store_true",
        help="Keep oldest version of duplicates instead of newest"
    )
    args = parser.parse_args()
    
    deduplicator = ModernDeduplicator(args.path)
    stats = await deduplicator.deduplicate(keep_newest=not args.keep_oldest)

if __name__ == "__main__":
    asyncio.run(main())
