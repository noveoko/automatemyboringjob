import pandas as pd
import numpy as np
from pathlib import Path
import os
from PIL import Image
from matplotlib import pyplot as plt
import sys
from glob import glob
import hashlib


def path_to_image(path=Path(r"C:\Users\mrkra\Downloads\IMG_20210815_095915.jpg"), show=False):
    assert os.path.exists(path)
    image = Image.open(path)
    print(image.format, image.size, image.mode)
    if show:
        image.show()
    return image


def resize_image(image, x, y, show=False):
    new_image = image.resize((x, y))
    if show:
        image.show()
    return new_image


def convert_to_mode(image, mode="1", show=False):  # L, 1, RGBA
    n = image.convert(mode)
    if show:
        n.show()
    return n


def image_to_array(image, show=False):
    array = np.array(image)
    if show:
        print(array)
    return array


def image_to_dateframe(array, show=False):
    df = pd.DataFrame(array)
    if show:
        plt.imshow(df)
    return df


def hash_every_image_in_directory(new_x=10, new_y=10, path=Path(r"C:/Users/mrkra/Documents/Projects/PanamMissing/")):
    extensions = ["jpg", "jpeg", "png", "gif", "tif"]
    hashes_with_files = {}
    for ext in extensions:
        files = (glob(f"{path}/*.{ext}"))
        for file in files:
            image = path_to_image(file)
            small = resize_image(image, new_x, new_y)
            # save resized image
            stem = Path(file).stem
            small_reduced = convert_to_mode(small, "1")
            # small_reduced.save(f"images/{stem}_small.jpg")
            small_as_bytes = image_to_array(small_reduced)
            hash = hashlib.sha384(small_as_bytes).hexdigest()
            if hash not in hashes_with_files.keys():
                hashes_with_files[hash] = []
                hashes_with_files[hash].append(file)
            else:
                hashes_with_files[hash].append(file)
    return hashes_with_files


if __name__ == "__main__":
    path = sys.argv[1]
    if path:
        try:
            hashes = hash_every_image_in_directory(path=Path(path))
            for key, matches in hashes.items():
                if len(matches) > 1:
                    print(f"{key}:{matches}")
        except Exception as e:
            print(e)
