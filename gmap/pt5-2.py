import requests
import json
import time
from bs4 import BeautifulSoup
from turtle import color
import gmplot


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

n = 1
taichungs = []
needcounty = "臺中市"
gmap = gmplot.GoogleMapPlotter(24.227079, 120.583611, 7)

print("========== Gmap Marker List ==========")
for site in jsondata:
    SiteName = site["sitename"]
    county = site["county"]
    Lat = site["twd97lat"]
    Lon = site["twd97lon"]
    if(county == needcounty):
        color = 'red'
    else:
        color = 'blue'

    print("{} 站名:{}({},{})[{}]".format(
        n, SiteName, Lat, Lon, color))

    n += 1

    Lat = float(Lat)
    Lon = float(Lon)

    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s"
    gmap.marker(Lat, Lon, color, title=SiteName)

gmap.draw("PM25-Gmap.html")


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
    ftp.quit()


Upload("PM25-Gmap.html")
