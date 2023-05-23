spam = ['apples', 'bananas', 'tofu', 'cats']

def commaFunc(li):
    sentence = ''
    for i, val in enumerate(li):
        if len(li) == 0:
            return None
        if len(li) == 1:
            return val

        if i == len(li) - 1:
           sentence += 'and ' + val
        else:
            sentence += val + ', '
    return sentence

print(commaFunc(spam))
