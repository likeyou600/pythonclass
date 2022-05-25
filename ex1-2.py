import requests

url = 'https://www.lib.pu.edu.tw/history/lukinglocation.html'

html = requests.get(url)

html.encoding = 'utf-8'

list = html.text.splitlines()
print("*************", list)
c = 0

for row in list:
    print('======================================================')
    c += 1
    print("***L%d:" % c)
    print(row)
