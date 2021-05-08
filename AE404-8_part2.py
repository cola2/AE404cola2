import time
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys 

chrome = webdriver.Chrome()
chrome.get('https://pic.sogou.com')
inputBar = chrome.find_element_by_class_name('query.query-defalut')
inputBar.send_keys('puppy')

# inputBar.send_keys(Keys.ENTER)
button = chrome.find_element_by_class_name('search-btn')
button.click()
time.sleep(2)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(2)
chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(2)


index = 1
for element in chrome.find_elements_by_css_selector('[lazy = "loaded"]'):
	flag = False
	img_url = element.get_attribute('src')
	
	try:
		imgRespond = requests.get(img_url, timeout = 5)
	except (requests.exceptions.Timeout):
		print('error!')
		flag = True

	if flag == False:
		with open(str(index) + '.jpg', 'wb') as f:
			f.write(imgRespond.content)
		index += 1

	else:
		continue

	if index > 30:
		break

