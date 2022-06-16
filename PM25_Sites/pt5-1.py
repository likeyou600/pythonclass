import sqlite3
import hashlib
import os
import requests
import json
import time
from bs4 import BeautifulSoup


conn = sqlite3.connect('PM25_Sites.sqlite')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS TableSites("no" INTEGER PRIMARY KEY AUTOINCREMENT,"SiteName" TEXT NOT NULL UNIQUE,"County" TEXT NOT NULL,    "Latitude" REAL,    "Longitude" REAL,    "Address" TEXT)'
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


url = "https://data.epa.gov.tw/api/v2/aqx_p_07?api_key=11b06bab-52bf-48c8-a743-72ad5d32181a&format=json"
html = requests_html(url).encode('utf-8')

new_md5 = hashlib.md5(html).hexdigest()
old_md5 = ""
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r')as f:
        old_md5 = f.read()
with open('old_md5.txt', 'w')as f:
    f.write(new_md5)

if new_md5 != old_md5:
    print('資料已更新...')
    print('=========================================')
    sp = BeautifulSoup(html, 'html.parser')
    jsondata = json.loads(sp.text)
    jsondata = jsondata['records']

    cursor.execute("delete from TableSites")
    conn.commit()

    n = 1
    taichungs = []
    needcounty = "臺中市"
    for site in jsondata:
        SiteName = site["sitename"]
        county = site["county"]
        Lat = site["twd97lat"]
        Lon = site["twd97lon"]
        addr = site["siteaddress"]
        print("{} 站名:{}({})  Lat={}  Lon={}".format(
            n, SiteName, county, Lat, Lon))

        if(county == needcounty):
            taichungs.append(
                "站名:{}  Lat={}  Lon={}  Address:{}".format(SiteName, Lat, Lon, addr))

        cursor.execute(
            "INSERT INTO TableSites values({},'{}','{}',{},{},'{}')".format(n, SiteName, county, Lat, Lon, addr))
        n += 1
    conn.commit()
    print("=================="+needcounty + "=====================")
    for taichung in taichungs:
        print(taichung)
else:
    print('資料未更新...')
    print('=========================================')
    cursor = cursor.execute("SELECT * from TableSites")
    rows = cursor.fetchall()
    needcounty = "臺中市"
    taichungs = []
    for row in rows:
        n = row[0]
        SiteName = row[1]
        county = row[2]
        Lat = row[3]
        Lon = row[4]
        addr = row[5]
        print("{} 站名:{}({})  Lat={}  Lon={}".format(
            n, SiteName, county, Lat, Lon))

        if(county == needcounty):

            taichungs.append(
                "站名:{}  Lat={}  Lon={}  Address:{}".format(SiteName, Lat, Lon, addr))
    print("=================="+needcounty + "=====================")
    for taichung in taichungs:
        print(taichung)
conn.close()
