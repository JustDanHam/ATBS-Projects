#! python3
# copyText.py - copys and pastes all text in open files with winTitle in the
# title. Returns a list


import pyautogui
import pyperclip


def copyText(winTitle):
    """Copies all text in open files with winTitle in title, returns a list."""

    windows = pyautogui.getWindowsWithTitle(winTitle)
    textList = []

    for window in windows:
        window.minimize()
        window.maximize()
        window.restore()
        pyautogui.click(200, 200)
        if not window.isActive:
            print(f'Error: {window.title} is not active and will be skipped.')
            continue
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        text = pyperclip.paste()
        textList.append(text)

    return textList


if __name__ == '__main__':
    winTitle = input('Input string to search for in window titles: ')
    print(copyText(winTitle))
