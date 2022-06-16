# 2022-05-23
# 2022-05-24
from ftplib import FTP
import time
import sqlite3
from bokeh.plotting import figure, output_file, show


# cur_path = os.path.dirname(__file__)
# conn = sqlite3.connect(cur_path+'/'+'DataBasePM25.sqlite')


def main(needcounty, inputdate):
    conn = sqlite3.connect('DataBasePM25.sqlite')
    cursor = conn.cursor()

    likeinputdate = inputdate+"%"

    cursor = cursor.execute(
        "SELECT * from TablePM25 where DataCreationDate LIKE ? AND county=? ORDER BY DataCreationDate", (likeinputdate, needcounty,))
    rows = cursor.fetchall()

    if(rows == []):
        return False
    else:
        print("===== "+needcounty+"["+inputdate+"] =====")

        mycount = 0
        # 折線圖用
        city_pm = [list() for _ in range(5)]
        listxsame = []
        # 折線圖用

        for row in rows:

            SiteName = row[0]
            PM25 = row[1]
            time = row[3]
            time = time[11:]
            if(mycount % 5 == 0):
                print(time)
                listxsame.append(time[:2]+"h")
                mycount = 0
            city_pm[mycount].append(PM25)

            print("站名:{}  PM2.5={}".format(SiteName, PM25))

            mycount += 1

        # 折線圖
        p = figure(x_range=listxsame, width=800,
                   height=400, title="臺中市PM2.5["+inputdate+"]")
        # x軸的名稱及樣式
        p.xaxis.axis_label = "Time"
        p.xaxis.axis_label_text_color = "black"
        # y軸的名稱及樣式
        p.yaxis.axis_label = "PM2.5"
        p.yaxis.axis_label_text_color = "black"

        p.line(listxsame, city_pm[0], line_color="red",
               legend_label="西屯")
        p.line(listxsame, city_pm[1], line_color="blue",
               legend_label="忠明")
        p.line(listxsame, city_pm[2], line_color="green",
               legend_label="大里")
        p.line(listxsame, city_pm[3], line_color="black",
               legend_label="沙鹿")
        p.line(listxsame, city_pm[4], line_color="orange",
               legend_label="豐原")

        output_file("PM25line.html")
        # show(p)
        # 折線圖

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
        fname = 'PM25line.html'
        tname = 'PM25line.html'
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


needcounty = "臺中市"
inputdate = input("請輸入日期(yyyy-mm-dd):")
while(main(needcounty, inputdate) == False):
    print("***無該日監測資料，請重新輸入")
    inputdate = input("請輸入日期(yyyy-mm-dd):")
