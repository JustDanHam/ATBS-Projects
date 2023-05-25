import re


def checkDate(date):
    dateRegex = re.compile(r'(\d\d)/(\d\d)/([12]\d{3})')
    dateSearch = dateRegex.search(date)
    if dateSearch is None:
        print('Error: Input is not a date in the DD/MM/YYYY format.')
        return
    day, month, year = dateSearch.groups()
    thirtyDayMonths = ['04', '06', '09', '11']
    thirtyOneDayMonths = ['01', '03', '05', '07', '08', '10', '12']
    correctDate = False

    if (1 <= int(day) <= 30) and (month in thirtyDayMonths):
        correctDate = True
    elif (1 <= int(day) <= 31) and (month in thirtyOneDayMonths):
        correctDate = True
    elif (day == '28') and (month == '02'):
        correctDate = True
    elif (day == '29') and (month == '02') and (int(year) % 4 == 0):
        if (int(year) % 100 == 0) and (int(year) % 400 == 0):
            correctDate = True
        elif int(year) % 100 == 0:
            correctDate = False
        else:
            correctDate = True

    if correctDate:
        print('This is a correctly formatted date')
    else:
        print('This is not a date in the correct DD/MM/YYYY format')


if __name__ == '__main__':
    date = input('Enter a date in the DD/MM/YYYY format: ')
    checkDate(date)
