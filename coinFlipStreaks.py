import random


numberOfStreaks = 0
streak = 1

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
            flips.append(random.randint(0, 1))

    # Checks how many streaks of h/t (0/1) there are.
    for idx, flip in enumerate(flips):
        if flip == flips[idx - 1]:
            if idx == 0:    # Prevents a wrap around streak being counted.
                continue
            streak += 1     # Adds 1 to streak count
        else:
            streak = 1      # If current flip doesn't match previous, reset streak.
        if streak == 6:
            numberOfStreaks += 1
            streak = 1

streaksPer100 = numberOfStreaks / 10000

print('Total streaks of 6 heads/ tails: ' + str(numberOfStreaks))
print('Chance of a streak of 6 heads/ tails after 100 flips: ' + str(int(streaksPer100 * 100))+ '%')
