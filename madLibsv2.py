import random, re


madLibsList = ['The ADJECTIVE panda walked to the NOUN and then \
VERB. A nearby NOUN was unaffected by these events.']

madLibsText = random.choice(madLibsList)
madLibsWordList = re.findall(r'\w+|[^\s\w]+', madLibsText)
adjNouAdvVerList = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for idx, i in enumerate(madLibsWordList):
    if i in adjNouAdvVerList:
        madLibsWordList[idx] = input(f'Enter {i}: ')

madLibsWordString = ' '.join(madLibsWordList)
print(madLibsWordString)
