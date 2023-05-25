#! python3
# fillingInTheGaps.py
# Write a program that finds all files with a given prefix, such as
# spam001.txt, spam002.txt, and so on, in a single folder and locates
# any gaps in the numbering (such as if there is a spam001.txt and
# spam003.txt but no spam002.txt). Have the program rename all the later
# files to close this gap.

import re, os, sys


while True:
    chosenDir = input('Choose the directoy to search in: ')
    chosenDir = os.path.abspath(chosenDir)
    if os.path.isdir(chosenDir):
        break
    else:
        print('Folder does not exist.')

filenameList = os.listdir(chosenDir)

inputPrefix = input('Enter the prefix of the files to search through: ')
filePattern = re.compile(rf'^({inputPrefix}0*)(\d+)(.*?)$')

filenameList = list(filter(filePattern.search, filenameList))
if not filenameList:
    print('No file names matching that description. Goodbye')
    sys.exit()

filenameList.sort(key = lambda fn: int(re.search(filePattern, fn)[2]))

for count, filename in enumerate(filenameList, 1):
    mo = filePattern.search(filename)
    beforeNum = mo.group(1)
    fileNum = mo.group(2)
    afterNum = mo.group(3)

    oldFilename = f'{chosenDir}\\{filename}'
    newFilename = f'{chosenDir}\\{beforeNum}{count}{afterNum}'
    print(f'{oldFilename} renamed to {newFilename}')
    os.rename(oldFilename, newFilename)



