import requests
from bs4 import BeautifulSoup
url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")

# 威力彩區塊
data2 = data1[0].find('div', {'class': 'contents_box02'})

# 上方標題
title = data2.find('span', {'class': 'font_black15'})
print(title.string)

# 中文文字
chinese = data2.find('div', {'class': 'contents_mine_tx04'})

data3 = data2.find_all('div', {'class': 'ball_tx'})
redball = data2.find('div', {'class': 'ball_red'})
first = chinese.text[0:4]+" : "
second = chinese.text[4:8]+" : "
for i in range(0, 6):
    first += data3[i].string

for i in range(6, 12):
    second += data3[i].string
print('-----------------------------------------')
print(first)
print(second)
print(chinese.text[8:11]+" : "+redball.string)
