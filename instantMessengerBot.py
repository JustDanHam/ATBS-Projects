#! python3
# instantMessengerBot.py - Sends a facebook message to each person in a
# list of names.
# Must already be logged into facebook.

import webbrowser
import pyautogui
from time import sleep


message = 'Hello, I am a robot. Beep boop.'

friendList = ['friend1', 'friend2']

pyautogui.PAUSE = 0.5

webbrowser.open('https://www.facebook.com/messages')
sleep(5)
messengerWindow = pyautogui.getActiveWindow()
messengerWindow.maximize()

for friend in friendList:
    pyautogui.click(50, 200)
    pyautogui.write(friend)
    pyautogui.click(100, 300)
    sleep(1)
    pyautogui.write(message)
    pyautogui.press('enter')
    sleep(1)
