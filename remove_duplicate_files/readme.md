# Modern File Deduplicator

A high-performance Python utility for finding and removing duplicate files using asynchronous I/O and parallel processing.

## Features

- Fast file scanning using async I/O and parallel processing
- xxHash for efficient file hashing
- Progress bars and rich logging
- Detailed statistics about space saved and files processed
- Option to keep either newest or oldest duplicate files
- Comprehensive error handling and reporting

## Requirements

- Python 3.10 or higher
- Required packages:
  ```
  aiofiles
  rich
  xxhash
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/modern-deduplicator.git
   cd modern-deduplicator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line

Basic usage:
```bash
python deduplicator.py /path/to/scan
```

Keep oldest files instead of newest:
```bash
python deduplicator.py /path/to/scan --keep-oldest
```

### As a Library

```python
from deduplicator import ModernDeduplicator
import asyncio

async def deduplicate_files():
    deduplicator = ModernDeduplicator("/path/to/scan")
    stats = await deduplicator.deduplicate(keep_newest=True)
    print(stats)

asyncio.run(deduplicate_files())
```

## Safety Features

- Dry run option (coming soon)
- Detailed logging of all operations
- Error recovery and graceful failure
- Custom exceptions for better error handling

## Performance

The deduplicator uses several techniques to maximize performance:
- Async I/O for file operations
- Process pool for CPU-bound hashing
- Chunked file reading
- xxHash for fast hashing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use and modify as needed.

## Safety Warning

Always backup important data before running deduplication tools. While this tool is designed to be safe, mistakes in identifying duplicates could potentially lead to data loss.
