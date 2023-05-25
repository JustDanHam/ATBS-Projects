from pathlib import Path
import re


while True:
    # Ask user to input a directory, and exit the loop if it is valid.
    userDir = Path(input('Enter the path of the folder you want to search in: '))
    if userDir.is_dir():
        break
    else:
        print('Please enter a valid directory')


userRegex = re.compile(input('Enter a regex to search for: '))
print()

# Find .txt files and search them for the userRegex, line by line.
for textFilePath in userDir.glob('*.txt'):
    textFile = open(textFilePath)
    textFileContents = textFile.readlines()
    filteredFileContents = list(filter(userRegex.search, textFileContents))

    # Print every line that userRegex is found in.
    if len(filteredFileContents) == 0:
        print(f'0 matches in {textFilePath.name}\n')
    else:
        print(f'{len(filteredFileContents)} matches in {textFilePath.name}:\n')
        for i in filteredFileContents:
            print(i)
        print()
