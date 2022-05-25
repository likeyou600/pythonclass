from itertools import count
import requests
from bs4 import BeautifulSoup
url = 'https://www.etax.nat.gov.tw/etw-main/ETW183W1/'
html = requests.get(url)

sp = BeautifulSoup(html.text, 'html.parser')

# 網址區塊
data_1 = sp.select("#page1")

# 11~12月網址取得
data_2 = data_1[0].find_all('a')

# 避免出現清冊排第一
if (data_2[0].get('href')[28:29] == '2'):
    newurl = 'https://www.etax.nat.gov.tw'+data_2[0].get('href')[11:35]
else:
    newurl = 'https://www.etax.nat.gov.tw'+data_2[1].get('href')[11:35]
newurl = 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_10907/'
# newurl = 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_11011/'
html = requests.get(newurl)
html.encoding = "utf-8"
sp = BeautifulSoup(html.text, 'html.parser')

# 發票區塊
data_1 = sp.select("#tenMillionsTable")

# 上方標題

data_2 = data_1[0].find('td')
print(data_2.string)
print('=======================================')
chinese = data_1[0].find_all('th')

number = data_1[0].find_all('div', {'class': 'col-12 mb-3'})

print(chinese[1].string+": "+number[0].string.strip())
print(chinese[2].string+": "+number[1].string.strip())
print(chinese[3].string+": "+number[2].string.strip()+" " +
      number[3].string.strip()+" "+number[4].string.strip())
if len(number) >= 6:
    mooresix = ''
    for i in range(len(number)-5):
        mooresix += number[i+5].string.strip()+" "
print(chinese[9].string+": "+mooresix)

print('=======================================')
