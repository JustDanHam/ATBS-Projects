#! python3
# convertingSpreadsheetsToOtherFormats.py - uploads a spreadsheet to Google
# Sheets, then downloads it in other formats.

import ezsheets


spreadsheetFile = input('Enter the name of the spreadsheet to convert: ')
ss = ezsheets.upload(spreadsheetFile)
ss.downloadAsPDF()
print(f'Done! {ss.title} has been converted to a .PDF')
