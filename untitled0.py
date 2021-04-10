import re
gmail = input("輸入你的gmail")

if re.fullmatch("\w+@gmail.com$", gmail) != None:
    print('對了!')
    
else:
    print("錯了motherfucker")