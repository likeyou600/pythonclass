import requests
import re

url = 'https://www.taiwanlottery.com.tw/lotto649/index.asp'
html = requests.get(url)
html.encoding = 'utf-8'

list = html.text.splitlines()

c = 1

countrow = 1

for row in list:
    ms = re.findall('[0-9]+、[0-9]+[、[0-9]+]*', row)
    if(ms):
        print('-----------------------------------')
        print("***L"+str(countrow)+" : "+str(ms)[2:-2])
        print(re.findall('[0-9]+', str(ms)))
        countrow += 1
    c += 1

print('-----------------------------------')
print("總共: "+str(countrow-1)+" 個數字列")
