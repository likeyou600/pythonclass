import sqlite3
import hashlib
import os
import time
import requests
import json
from bs4 import BeautifulSoup

cur_path = os.path.dirname(__file__)
conn = sqlite3.connect(cur_path+'/'+'TablePM25.sqlite')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS TablePM25("SiteName" TEXT NOT NULL ,"PM25" INTEGER NOT NULL,"county" TEXT NOT NULL,"DataCreationDate" Text NOT NULL,"InsertNo" INTEGER NOT NULL)'
cursor.execute(sqlstr)


def requests_html(url):
    while True:
        try:
            html = requests.get(url).text
            if (html == '請勿頻繁索取資料,一分鐘呼叫API的次數不可大於1次'):
                time.sleep(60)
            else:
                return html
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")


url = "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=11b06bab-52bf-48c8-a743-72ad5d32181a&format=json"
html = requests_html(url).encode('utf-8')

new_md5 = hashlib.md5(html).hexdigest()
old_md5 = ""
if os.path.exists(cur_path+'/'+'old_md5.txt'):
    with open(cur_path+'/'+'old_md5.txt', 'r')as f:
        old_md5 = f.read()
with open(cur_path+'/'+'old_md5.txt', 'w')as f:
    f.write(new_md5)

if new_md5 != old_md5:
    print('*** 資料已更新...')
    sp = BeautifulSoup(html, 'html.parser')
    jsondata = json.loads(sp.text)
    jsondata = jsondata['records']

    n = 1
    taichungs = []
    needcounty = "臺中市"

    cursor = cursor.execute(
        "SELECT InsertNo from TablePM25 ORDER BY InsertNo DESC")
    rows = cursor.fetchone()
    InsertNo = 1 if rows == None else int(rows[0])+1
    print("*** currentInsertNo =  "+str(InsertNo))
    print('============= 全國最新PM2.5資訊 =============')

    for site in jsondata:
        SiteName = site["site"]
        PM25 = 0 if site["pm25"] == "" else int(site["pm25"])
        county = site["county"]
        datacreationdate = site['datacreationdate']
        print("{} 站名:{}({}) PM2.5={} Date={}".format(
            n, SiteName, county, PM25, datacreationdate))
        n += 1
        cursor.execute("INSERT INTO TablePM25 values('{}',{},'{}','{}',{})".format(
            SiteName, PM25, county, datacreationdate, InsertNo))
    conn.commit()

    needcounty = "臺中市"
    if InsertNo >= 3:
        for i in range(InsertNo, InsertNo-3, -1):
            cursor = cursor.execute(
                "SELECT * from TablePM25 where InsertNo=? AND county=?", (i, needcounty))
            rows = cursor.fetchall()
            print("========== "+needcounty +
                  "["+rows[0][3]+"] ==========")
            for row in rows:
                SiteName = row[0]
                PM25 = row[1]
                county = row[2]

                if(PM25 < 36):
                    color = '綠'
                elif(PM25 < 53):
                    color = '黃'
                elif(PM25 < 71):
                    color = '紅'
                elif(PM25 >= 71):
                    color = '紫'
                print(
                    "站名:{}  PM2.5={} ***{}***".format(SiteName, PM25, color))
    else:
        print("添加資料中")
else:
    print('*** 資料未更新...')
    cursor = cursor.execute(
        "SELECT InsertNo from TablePM25 ORDER BY InsertNo DESC")
    rows = cursor.fetchone()
    InsertNo = int(rows[0])
    print("*** currentInsertNo =  "+str(InsertNo))
    print('============= 全國最新PM2.5資訊 =============')

    cursor = cursor.execute(
        "SELECT * from TablePM25 WHERE InsertNo =?", (InsertNo,))
    rows = cursor.fetchall()
    n = 1
    for row in rows:
        SiteName = row[0]
        PM25 = row[1]
        county = row[2]
        DataCreationDate = row[3]
        print("{} 站名:{}({}) PM2.5={} Date={}".format(
            n, SiteName, county, PM25, DataCreationDate))
        n += 1

    needcounty = "臺中市"
    if InsertNo >= 3:
        for i in range(InsertNo, InsertNo-3, -1):
            cursor = cursor.execute(
                "SELECT * from TablePM25 where InsertNo=? AND county=?", (i, needcounty))
            rows = cursor.fetchall()
            print("========== "+needcounty +
                  "["+rows[0][3]+"] ==========")
            for row in rows:
                SiteName = row[0]
                PM25 = row[1]
                county = row[2]

                if(PM25 < 36):
                    color = '綠'
                elif(PM25 < 53):
                    color = '黃'
                elif(PM25 < 71):
                    color = '紅'
                elif(PM25 >= 71):
                    color = '紫'
                print(
                    "站名:{}  PM2.5={} ***{}***".format(SiteName, PM25, color))
    else:
        print("添加資料中")
conn.close()
input('Completed!')
