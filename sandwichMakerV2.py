import pyinputplus as pyip, pprint


sandwichItems = {
                'breadType': {'wheat': 1.00, 'white': 1.00, 'sourdough': 1.50},
                'proteinType': {'chicken': 1.00, 'turkey': 1.10, 'ham': 1.20, 'tofu': 1.30, 'peanut butter': 5.00},
                'cheeseType': {'cheddar': 1.00, 'Swiss': 1.50, 'mozzarella': 1.50},
                'extras': {'mayo': 0.10, 'mustard': 0.15, 'lettuce': 0.05, 'tomato': 0.10}
                }

sandwichChoice = {}
extrasNumber = 0
totalPrice = 0.0


print('WELCOME TO DAN HAM\'S SAMS \n')

sandwichChoice['breadType'] = pyip.inputMenu(list(sandwichItems['breadType'].keys()), numbered=True)
sandwichChoice['proteinType'] = pyip.inputMenu(list(sandwichItems['proteinType'].keys()), numbered=True)
cheeseYN = pyip.inputYesNo('Would you like cheese? ')
if cheeseYN == 'yes':
    sandwichChoice['cheeseType'] = pyip.inputMenu(list(sandwichItems['cheeseType'].keys()), numbered=True)
for i in sandwichItems['extras'].keys():
    extraYN = pyip.inputYesNo(f'Would you like {i}? ')
    if extraYN == 'yes':
        extrasNumber += 1
        sandwichChoice[f'extra {extrasNumber}'] = i

for k, v in sandwichItems.items():
    for i, j in sandwichItems[k].items():
        if i in sandwichChoice.values():
            totalPrice += j

print('-------------------------')
print('Your order: ')
print('-------------------------')
for k, v in sandwichChoice.items():
    print(f'{k.ljust(12)}{":".ljust(2)}{v}')
print('-------------------------')
print(f'That will be £{totalPrice:.2f}')
