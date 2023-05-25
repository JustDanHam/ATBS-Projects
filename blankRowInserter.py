#! python3
# blankRowInserter.py - takes two integers and a filename string as command
# line arguments. First integer (N) being place to insert blank rows, and
# the second (M) being how many rows.

import sys
import openpyxl
import os


N = int(sys.argv[1])
M = int(sys.argv[2])
filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
sheet = wb.active
sheet.insert_rows(N, amount=M)
wb.save(f'{os.path.splitext(filename)[0]}Copy.xlsx')
