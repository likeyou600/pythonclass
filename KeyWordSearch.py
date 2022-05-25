import requests
import re

url = 'https://www.taiwanlottery.com.tw/lotto649/index.asp'
html = requests.get(url)
html.encoding = 'utf-8'

search = input('請輸入關鍵字:')

list = html.text.splitlines()

c = 1

countrow = 0
counttime = 0

for row in list:
    m = re.findall(search, row)
    if(m):
        print('-----------------------------------')
        print("***L"+str(c)+":("+str(len(m))+"):")
        print(row)
        countrow += 1
        counttime += len(m)
    c += 1

print('-----------------------------------')
print("找到"+str(countrow)+"行有普獎")
print("找到"+str(counttime)+"次普獎")
