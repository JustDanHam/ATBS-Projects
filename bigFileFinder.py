#! python3
# bigFileFinder.py - finds files in chosen folder tree above the
# requested size (in MB), and prints them to the screen.

import os


def bigFileFinder(folder, size):

    folder = os.path.abspath(folder)
    foundFiles = []

    if os.path.exists(folder):
        for folderName, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                fileSize = os.path.getsize(filePath) / (1024*1024)
                if fileSize > int(size):
                    print(f'File {filename} in folder {folderName} is {fileSize:.2f}MB\n')
                    foundFiles += [filePath]
    else:
        print(f'{folder} not found')

    if len(foundFiles) == 0:
        print(f'No files above {size}MB in {folder}')

    return foundFiles


inputFolder = input('Enter folder to start the search from: ')
inputSize = input('Enter min size of file in MB: ')

bigFileFinder(inputFolder, inputSize)
