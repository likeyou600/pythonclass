import sqlite3
import hashlib
import os
import requests
import json
from bs4 import BeautifulSoup


conn = sqlite3.connect('DataBasePM25.sqlite')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS TablePM25("no"INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)'
cursor.execute(sqlstr)


url = "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=11b06bab-52bf-48c8-a743-72ad5d32181a&format=json"

html = requests.get(url).text.encode('utf-8')
if(len(html) == 70):
    print('請勿頻繁索取資料 一分鐘呼叫API次數不可大於一次')
else:
    new_md5 = hashlib.md5(html).hexdigest()
    old_md5 = ""
    if os.path.exists('old_md5.txt'):
        with open('old_md5.txt', 'r')as f:
            old_md5 = f.read()
    with open('old_md5.txt', 'w')as f:
        f.write(new_md5)

    if new_md5 != old_md5:
        print('資料已更新，分析新資料...')
        print('=========================================')
        sp = BeautifulSoup(html, 'html.parser')
        jsondata = json.loads(sp.text)
        jsondata = jsondata['records']
        print(jsondata)
        print('=========================================')
        print('清空資料庫，寫入新資料')
        print('=========================================')
        cursor.execute("delete from TABLEPM25")
        conn.commit()

        n = 1
        for site in jsondata:
            SiteName = site["site"]
            PM25 = 0 if site["pm25"] == "" else int(site["pm25"])
            print("{} 站名:{}  PM2.5={}".format(n, SiteName, PM25))

            cursor.execute(
                "INSERT INTO TablePM25 values({},'{}',{})".format(n, SiteName, PM25))
            n += 1
        conn.commit()
    else:
        print('資料未更新 從資料庫讀取')
        print('=========================================')
        cursor = cursor.execute("SELECT * from TablePM25")
        rows = cursor.fetchall()
        for row in rows:
            print("{} 站名:{}  PM2.5={}".format(row[0], row[1], row[2]))
    conn.close()
