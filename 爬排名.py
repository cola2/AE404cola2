import requests
from bs4 import BeautifulSoup
url = 'https://www.books.com.tw/web/sys_saletopb/books/'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

divs = soup.find_all('div', class_='nolist')

for each_div in divs:
    
    a = each_div.find('a')
    bookname = a.text
    print(bookname)
