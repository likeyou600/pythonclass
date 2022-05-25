import hashlib
import os
import requests
url = "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=11b06bab-52bf-48c8-a743-72ad5d32181a&format=json"

html = requests.get(url).text.encode('utf-8')

if(len(html) == 70):
    print('請勿頻繁索取資料 一分鐘呼叫API次數不可大於一次')
else:
    new_md5 = hashlib.md5(html).hexdigest()
    old_md5 = " "
    if os.path.exists('old_md5.txt'):
        with open('old_md5.txt', 'r')as f:
            old_md5 = f.read()
    with open('old_md5.txt', 'w')as f:
        f.write(new_md5)

    if new_md5 != old_md5:
        print('資料已更新分析新資料並寫入資料庫')
    else:
        print('資料未更新 從資料庫提取')
