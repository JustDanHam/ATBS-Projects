import re


lengthRegex = re.compile(r'.{8,}')
uppercaseRegex = re.compile(r'[A-Z]+')
lowercaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')
symbolsRegex = re.compile(r'[%&@\\\/\?\"\.]+')

def checkPassword(password):
    if lengthRegex.search(password) is not None:
        if uppercaseRegex.search(password) is not None:
            if lowercaseRegex.search(password) is not None:
                if symbolsRegex.search(password) is not None:
                    return 'Your password should not have symbols in it'
                elif digitRegex.search(password) is not None:
                    return 'Your password is strong AF'
    return 'Your password is weak AF'

print(checkPassword('BeBo31211CoDiPe'))
