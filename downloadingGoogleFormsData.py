#! python3
# downloadingGoogleFormsData.py - collects a list of the email addresses
# on a google spreadsheet created from data recieved through Google Forms.

import ezsheets


emailList = []

ss = ezsheets.Spreadsheet('yourSpreadsheetID')
sheet = ss['Form responses 1']
emailColumn = sheet.getColumn(3)
print(emailColumn)
