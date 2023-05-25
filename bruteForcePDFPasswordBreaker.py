#! python3
#bruteForcePDFPasswordBreaker.py

import PyPDF2


def pdfPassBreak(filename):

    pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
    dictFile = open('dictionary.txt', 'r')
    dictList = dictFile.read().splitlines()

    for word in dictList:
        print(f'Trying word: {word}')
        password = pdfReader.decrypt(word)
        passLower = pdfReader.decrypt(word.lower())
        if password:
            print(f'The password for "{filename}" is: {word}.')
            return word
        elif passLower:
            print(f'The password for "{filename}" is: {word.lower()}.')
            return word.lower

    print('Could not find password')


