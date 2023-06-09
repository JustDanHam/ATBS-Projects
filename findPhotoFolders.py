#! python3
# findPhotoFolders.py - Searches the entire C Drive for photo folders (a
# folder where at least half files are photos), and prints their paths.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith('.png')
                or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        try:
            # Open image file using Pillow.
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size

            # Check if width and height are larger than 500.
            if (width > 500) and (height > 500):
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1
        except OSError:
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(f'Found photo folder: {foldername}')
