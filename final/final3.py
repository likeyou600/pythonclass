import sqlite3

import requests
import json
import time
from bs4 import BeautifulSoup
import gmplot
from bokeh.plotting import figure, output_file, show


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

sp = BeautifulSoup(html, 'html.parser')
jsondata = json.loads(sp.text)
jsondata = jsondata['records']

cursor.execute("delete from TableSites")
conn.commit()

n = 1
needcounty = input("請輸入縣市:")
for site in jsondata:
    SiteName = site["sitename"]
    county = site["county"]
    Lat = site["twd97lat"]
    Lon = site["twd97lon"]
    addr = site["siteaddress"]
    cursor.execute(
        "INSERT INTO TableSites values({},'{}','{}',{},{},'{}')".format(n, SiteName, county, Lat, Lon, addr))
    n += 1
conn.commit()


url = "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=11b06bab-52bf-48c8-a743-72ad5d32181a&format=json"
html = requests_html(url).encode('utf-8')

sp = BeautifulSoup(html, 'html.parser')
jsondata = json.loads(sp.text)
jsondata = jsondata['records']

n = 1
gmap = gmplot.GoogleMapPlotter(24.227079, 120.583611, 7)

datatime = jsondata[0]["datacreationdate"]


# 直方圖用
allcity_name = []
allcity_pm = []
allcity_pm_color = []
# 直方圖用

mycheck = False
printtitle = False
for site in jsondata:
    SiteName = site["site"]
    PM25 = 0 if site["pm25"] == "" else int(site["pm25"])
    county = site["county"]

    if(county == needcounty):
        if(printtitle == False):
            print("======="+needcounty+" PM2.5即時資訊("+datatime + ") =======")
            printtitle = True

        mycheck = True
        color = ''
        if(PM25 < 36):
            color = '綠'
            markercolor = 'green'
            allcity_pm_color.append("green")

        elif(PM25 < 53):
            color = '黃'
            markercolor = 'yellow'
            allcity_pm_color.append("yellow")
        elif(PM25 < 71):
            color = '紅'
            markercolor = 'red'
            allcity_pm_color.append("red")
        elif(PM25 >= 71):
            color = '紫'
            markercolor = 'purple'
            allcity_pm_color.append("purple")

        allcity_name.append(SiteName)
        allcity_pm.append(PM25)

        print("{} 站名:{} PM2.5={} ***{}***".format(
            n, SiteName, PM25, color))
        n += 1

        cursor = cursor.execute(
            "SELECT * FROM TableSites WHERE SiteName = ?", (SiteName,))
        row = cursor.fetchone()
        Lat = row[3]
        Lon = row[4]

        Lat = float(Lat)
        Lon = float(Lon)

        gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s"
        gmap.marker(Lat, Lon, markercolor, title=SiteName+"("+str(PM25)+")")

if (mycheck == True):

    mapname = "PM25-Gmap-"+datatime[:10]+"-"+datatime[11:13]+".html"
    gmap.draw(mapname)

    # 直方圖
    q = figure(x_range=allcity_name,
               title=needcounty+"PM2.5["+datatime+"]")

    q.vbar(x=allcity_name, top=allcity_pm,
           width=0.1, color=allcity_pm_color)
    q.text(x=allcity_name, y=allcity_pm, text=allcity_pm)
    barname = "PM25-Bar"+datatime[:10]+"-"+datatime[11:13]+".html"
    output_file(barname)
    show(q)
    # 直方圖

    def Upload(htmlFile):

        from ftplib import FTP
        import time

        ftp = FTP()
        Not_CONNECT = True

        while Not_CONNECT:
            try:
                ftp.connect("files.000webhost.com", port=21, timeout=1000)
            except Exception as ErrorMessage:
                print("Error:", ErrorMessage)
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
            else:
                Not_CONNECT = False

        ftp.login('42s1081735', 's108173542')  # Website: 246 25
        ftp.cwd("public_html")  # Change directory
        fname = htmlFile
        tname = htmlFile

        try:
            f = open(fname, 'rb')
            ftp.storbinary('STOR ' + tname, f)
        except Exception as e:
            print('*** Upload Fail :', e)
        else:
            print("*** File %s uploaded!" % fname)
            url = "http://42s1081735.000webhostapp.com/" + fname
            print("*** URL: " + url)
            print("----------------------------------------------------")
        ftp.quit()

    print("====================================================")

    print("*** Generated: "+mapname+"")
    Upload(mapname)

    print("*** Generated: "+barname+"")
    Upload(barname)

    conn.close()
else:
    print("找不到該縣市")
