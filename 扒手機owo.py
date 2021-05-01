from selenium import webdriver
from bs4 import BeautifulSoup
import time


chrome = webdriver.Chrome()
chrome.get('https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone')
time.sleep(3)

for i in range(2):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
    
time.sleep(5)
pageSrc = chrome.page_source

soup = BeautifulSoup(pageSrc, 'html.parser')
chrome.close()

for prods in soup.find_all('h5', class_='prod_name'):
    print(prods.text)



