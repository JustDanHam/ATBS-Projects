#! python3
# findingMistakesInASpreadsheet.py

import ezsheets


ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for rowNum in range(2, len(ss[0].getRows()) + 2):
    if ss[0].getRow(rowNum)[0] == '':
        break
    if int(ss[0].getRow(rowNum)[0]) * int(ss[0].getRow(rowNum)[1]) != int(ss[0].getRow(rowNum)[2]):
        print(f'Found mistake. Incorrect total at row {rowNum}')
