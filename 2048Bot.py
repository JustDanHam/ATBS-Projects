#! python3
# 2048Bot - a program that automatically plays the game 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')
htmlElem = browser.find_element('tag name', 'html')
hiddenElem = browser.find_element('class name', 'retry-button')
while True:
    htmlElem.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    if hiddenElem.is_displayed():
        hiddenElem.click()
