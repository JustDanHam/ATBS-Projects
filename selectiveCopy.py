#! python 3
# selectiveCopy.py - Write a program that walks through a folder tree and
# searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import os, shutil


def selectiveCopy(folder, extension, destFolder):

    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)

    if not os.path.exists(destFolder):
        print(f'Creating {destFolder} as it does not exist.')
        os.makedirs(destFolder)

    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                print(f'Copying {filename} into folder {destFolder}.')
                shutil.copy(os.path.join(folderName, filename), destFolder)

inputFolder = input('Enter folder to walk through: ')
inputExt = input('Enter extension of the files you want to copy: ')
inputDestFolder = input('Enter the folder you want to copy the files to: ')

selectiveCopy(inputFolder, inputExt, inputDestFolder)
