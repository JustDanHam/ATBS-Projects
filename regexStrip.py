import re


def rgxStrip(s, char='\s'):
    if char == '':
        char = '\s'
    lStringRegex = re.compile('^[' + char + ']*')
    rStringRegex = re.compile('[' + char + ']*$')
    subString = lStringRegex.sub('', s)
    subString = rStringRegex.sub('', subString)
    return subString

text = '      Hello, my name is Dan. You can call me Dan.    '

print(text)
print(rgxStrip(text, ' '))
