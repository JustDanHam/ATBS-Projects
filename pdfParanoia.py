#! python3
# pdfParanoia.py - a script that will go through every PDF in a folder
# (and its subfolders) and encrypt the PDFs using a password provided
# on the command line.

import os
import sys
import PyPDF2


folder = sys.argv[1]
password = sys.argv[2]

folder = os.path.abspath(folder)

if os.path.exists(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                print(f'Encrypting {filename}...')
                filePath = os.path.join(folderName, filename)
                pdfFile = open(filePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted:
                    continue
                pdfWriter = PyPDF2.PdfFileWriter()
                pdfWriter.encrypt(password)
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                encryptedFilename = f'{filename[:-4]}_encrypted.pdf'
                encryptedFilePath = os.path.join(folderName, encryptedFilename)
                encryptedPdf = open(encryptedFilePath, 'wb')
                pdfWriter.write(encryptedPdf)
                pdfFile.close()
                encryptedPdf.close()

                encryptedPdf = open(encryptedFilePath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(encryptedPdf)
                if pdfReader.isEncrypted:
                    if pdfReader.decrypt(password):
                        print(f'{filename} has been successfully encrypted.')
                else:
                    print(f'Error. Could not encrypt {filename}')
else:
    print(f'{folder} not found.')

print('Finished')
