from itertools import count
import requests
from bs4 import BeautifulSoup
prize = ['特別獎', '特獎', '頭獎', '二獎', '三獎', '四獎', '五獎', '六獎', '沒中獎']

url = 'https://www.etax.nat.gov.tw/etw-main/ETW183W1/'
html = requests.get(url)

sp = BeautifulSoup(html.text, 'html.parser')

# 網址區塊
data_1 = sp.select("#page1")

# 兌獎網址取得
data_2 = data_1[0].find_all('a')

# 避免出現清冊排第一
if (data_2[0].get('href')[28:29] == '2'):
    newurl = 'https://www.etax.nat.gov.tw'+data_2[0].get('href')[11:35]
else:
    newurl = 'https://www.etax.nat.gov.tw'+data_2[1].get('href')[11:35]
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
# 增開六獎
if len(number) >= 6:
    mooresix = ''
    for i in range(len(number)-5):
        mooresix += number[i+5].string.strip()+" "
    print(chinese[9].string+": "+mooresix)
print('=======================================')

first = number[0].string.strip()
second = number[1].string.strip()
third_1 = number[2].string.strip()
third_2 = number[3].string.strip()
third_3 = number[4].string.strip()

prizes = [[first], [second], [third_1, third_2, third_3],
          [third_1[1:], third_2[1:], third_3[1:]], [
              third_1[2:], third_2[2:], third_3[2:]],
          [third_1[3:], third_2[3:], third_3[3:]], [third_1[4:], third_2[4:],
                                                    third_3[4:]], [third_1[5:], third_2[5:], third_3[5:]]]
if len(number) >= 6:
    mooresix = ''
    for i in range(len(number)-5):
        prizes[7].append(number[i+5].string.strip())

print('=======================================')
print(prizes)
print('=======================================')

for i in range(len(prizes)):
    print(prize[i]+" : "+str(prizes[i]))
print('=======================================')
while 1 == 1:
    inpput = input('Number:(-1 for exit)')
    if(inpput == '-1'):
        break
    if(len(inpput) >= 9):
        print('*** Error: 號碼長度有誤')
    else:
        nobingo = 1
        if(inpput == first):
            print(prize[0])
            nobingo = 0
        elif(inpput == second):
            print(prize[1])
            nobingo = 0

        if nobingo == 1:
            breaker = False
            for list in prizes:
                if breaker == True:
                    break
                for number in list:
                    if breaker == True:
                        break
                    if(number == inpput):
                        print(prize[prizes.index(list)])
                        nobingo = 0
                        breaker = True
                        break
                    else:
                        for cut in range(1, len(inpput)-2):
                            new = inpput[cut:]
                            if(number == new):
                                print(prize[prizes.index(list)])
                                nobingo = 0
                                breaker = True
                                break
        if nobingo == 1:
            print(prize[8])
        print('----------------------------')
