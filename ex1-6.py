import requests
from bs4 import BeautifulSoup
url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

sp = BeautifulSoap(html.text, 'html.parser')

print("--------------------(1)--------------------")
data1 = sp.select("title")
print(data1)

print("--------------------(2)--------------------")

data1 = sp.select("#rightdown")
print(data1)

print("--------------------(3)--------------------")
data1 = sp.select(".contents_box04")
print(data1)
print(data1[0])

print("--------------------(4)--------------------")
data1 = sp.select("html head totle")  # 逐層搜尋
print(data1)

print("--------------------(5))--------------------")
data1 = sp.select("html head")  # 逐層搜尋
print(data1)
