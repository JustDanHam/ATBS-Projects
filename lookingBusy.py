#! python3
# lookingBusy.py - Nudges the mouse cursor slighly every 10 seconds.

import pyautogui


pyautogui.PAUSE = 10

while True:
    pyautogui.move(1, 1)
