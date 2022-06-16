# 2022-05-23-21
# 2022-05-24-23
from ftplib import FTP
import time
import sqlite3
from bokeh.plotting import figure, output_file, show


# cur_path = os.path.dirname(__file__)
# conn = sqlite3.connect(cur_path+'/'+'DataBasePM25.sqlite')


def main(needcounty, inputdate):
    conn = sqlite3.connect('DataBasePM25.sqlite')
    cursor = conn.cursor()

    likeinputdate = inputdate[:10] + " "+inputdate[11:13]+":00"

    cursor = cursor.execute(
        "SELECT * from TablePM25 where DataCreationDate LIKE ? AND county=? ORDER BY DataCreationDate", (likeinputdate, needcounty,))
    rows = cursor.fetchall()
    if(rows == []):
        return False
    else:
        print("===== "+needcounty+"["+likeinputdate+"] =====")

        # 直方圖用
        allcity_name = []
        allcity_pm = []
        allcity_pm_color = []
        # 直方圖用

        for row in rows:
            SiteName = row[0]
            PM25 = row[1]
            if(PM25 < 36):
                color = '綠'
                allcity_pm_color.append("green")
            elif(PM25 < 53):
                color = '黃'
                allcity_pm_color.append("yellow")
            elif(PM25 < 71):
                color = '紅'
                allcity_pm_color.append("red")
            elif(PM25 >= 71):
                color = '紫'
                allcity_pm_color.append("purple")

            print(
                "站名:{}  PM2.5={} ***{}***".format(SiteName, PM25, color))

            allcity_name.append(SiteName)
            allcity_pm.append(PM25)

        # 直方圖
        q = figure(x_range=allcity_name,
                   title=needcounty+"PM2.5["+likeinputdate+"]")

        q.vbar(x=allcity_name, top=allcity_pm,
               width=0.1, color=allcity_pm_color)
        q.text(x=allcity_name, y=allcity_pm, text=allcity_pm)
        output_file("PM25bar.html")
        show(q)
        # 直方圖

        conn.close()
        print("========================================")

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

        ftp.login('43s1081754', 's108175443')  # Website: 246 25
        ftp.cwd("public_html")  # Change directory
        fname = 'PM25bar.html'
        tname = 'PM25bar.html'

        try:
            f = open(fname, 'rb')
            ftp.storbinary('STOR ' + tname, f)
        except Exception as e:
            print('*** Upload Fail :', e)
        else:
            print("*** File %s uploaded!" % fname)
            url = "http://43s1081754.000webhostapp.com/" + fname
            print("*** URL: " + url)
        ftp.quit()


needcounty = input("請輸入縣市:")
inputdate = input("請輸入日期時間(yyyy-mm-dd-hh):")
while(main(needcounty, inputdate) == False):
    print("*** 該時無監測資料，請重新輸入")
    inputdate = input("請輸入日期時間(yyyy-mm-dd-hh):")
