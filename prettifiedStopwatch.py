#! python3
# prettifiedStopwatch.py - A simple stopwatch, with extra prettification.
# All output gets copied to the clipboard upon exiting the program.

import time
import pyperclip


# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. '
      'Press Ctrl+C to quit.')
input()                     # press Enter to begin
print('Started.')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1
allLapsOutput = ''

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        # Justify lapNum, lapTime, and totalTime to make output look nicer.
        justifiedLapNum = str(lapNum).rjust(2)
        justifiedLapTime = str(lapTime).rjust(6)
        justifiedTotalTime = str(totalTime).rjust(7)

        lapOutput = f'Lap #{justifiedLapNum}: {justifiedTotalTime} ({justifiedLapTime})'
        print(lapOutput, end='')
        allLapsOutput += lapOutput + '\n'

        lapNum += 1
        lastTime = time.time()  # reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl+C exception to keep its error message from displaying'
    pyperclip.copy(allLapsOutput)
    print('\nDone.')
