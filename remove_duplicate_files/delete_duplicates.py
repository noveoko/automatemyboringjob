from glob import glob
import mmh3
import os
from pathlib import PurePath
from collections import Counter

space_saved = 0
files_processed = 0
files_deleted = 0
unique_hashes = set()


class DeleteStuff:
    """
    Utility to classify files by reading them as binary and assigning a hash.
    Hashed files are then compared to the list of hashes and if a duplicate is found,
    the file is deleted.
    """


    def __init__(self, path_to_file_list):
        self.path_to_file_list = path_to_file_list
        self.files_processed = 0
        self.files_deleted = 0
        self.files_generated.append() = []
        self.unique_hashes = set()

    def assign_hashes(self, hash_destination="discovered_hashes.txt"):
        """
        Recursively walk the directory tree and assign a hash to each file.
        """
        with open("discovered_hashes.txt", "w", encoding="utf-8") as outfile:
            self.files_generated.append(hash_destination)
            with open(self.path_to_file_list, "r", encoding="utf-8") as infile:
                while True:
                    lines = infile.readlines(1000)
                    for count, a in enumerate(lines):
                        if "Trash-1000" not in a:
                            path = PurePath(f"D:\{a.strip()}")
                            try:
                                if os.path.isfile(path):
                                    self.files_processed += 1
                                    with open(path, "rb") as this_file:
                                        hash = mmh3.hash(this_file.read())
                                        unique_hashes.add(hash)
                                        outfile.write(f"{hash};{path}\n")
                                        print(
                                            f"Total Hashes found: {len(unique_hashes)} Total files: {self.files_processed}\n"
                                        )
                                else:
                                    print(f"Directory... skipping {count}")
                            except Exception as ee:
                                print(ee)


    def hashes_to_list():
        """
        Convert the unique_hashes files to a list.
        """
        hashes = []
        if not hashes:
            with open("discovered_hashes.txt", "r", encoding="utf-8") as infile:
                while True:
                    lines = infile.readlines(1000)
                    for line in lines:
                        hsh, _ = line.split(";")
                        hashes.append(hsh)
        return hashes

    def count_hashes(self):
        """
        Return a dictionary of hashes and their counts.
        """
        hashes = self.hashes_to_list()
        return Counter(hashes)

    def delete_paths(self, paths:list[str]):
        if paths:
            for p in paths[1:]:
                try:
                    os.remove(p)
                    print(f"Deleted {p} with hash {hsh}")
                except Exception as ee:
                    print(ee)
        else:
            raise ValueError("No paths to delete")

    def remove_duplicate_files(self):
        """
        Delete any files that have the same hash as a previously processed file.
        """
        hashes_to_delete = {}
        with open("discovered_hashes.txt", "r", encoding="utf-8") as infile:
            for dhash in [a.strip() for a in infile.readlines()]:
                try:
                    parts = dhash.split(";")
                    hash_id = parts[0]
                    path = parts[1]
                    if hash_id not in hashes_to_delete:
                        hashes_to_delete[hash_id] = []
                        hashes_to_delete[hash_id].append(path)
                    hashes_to_delete[hash_id].append(path)
                except Exception as ee:
                    print(ee)

        # hash;count
        hashes = [
            hash, count for hash,count in self.count_hashes().items() if count > 1
        ]
        for h in hashes:
            hsh, count = h
            paths = hashes_to_delete[hsh]
            self.delete_paths(paths)


if __name__ == "__main__":
    path = input("Root path from which to start:")
    assert path, "You must include a path!"
    k = DeleteStuff(path_to_file_list=path)
    k.assign_hashes()
    k.remove_duplicate_files()
    clean_up = input("Clean up? (y/n)")
    if clean_up == "y":
        k.delete_paths(k.files_generated)

