import time
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('https://www.google.com')
inputBar = chrome.find_element_by_class_name('gLFyf.gsfi')
inputBar.send_keys('猿創力')
time.sleep(1)

button = chrome.find_element_by_class_name('gNO89b')
button.click()
time.sleep(1)

button = chrome.find_element_by_class_name('LC20lb.DKV0Md')
button.click()
time.sleep(1)

chrome.maxsize_window()
chrome.get_screenshot_as_file('123.png')









































