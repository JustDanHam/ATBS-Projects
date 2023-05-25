import pyinputplus as pyip
import random, time


numOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numOfQuestions):

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'{questionNumber + 1}: {num1} x {num2} = '

    question = pyip.inputInt(prompt, allowRegexes=[f'{num1 * num2}'], blockRegexes=[(f'.*', 'Incorrect!')], limit=3, timeout=8, default='Incorrect')

    if question == 'Incorrect':
        print(f'The answer was {num1 * num2}')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)

print(f'That\'s all folks! You scored: {correctAnswers}/{numOfQuestions}')
if correctAnswers <= 5:
    print(f'Ouch! Back to school you go.')
elif 5 < correctAnswers < 8:
    print(f'Hmm, not bad... I guess.')
elif 7 < correctAnswers < 10:
    print(f'Very good.')
else:
    print(f'Wow. Perfection. You\'re amazing!')
