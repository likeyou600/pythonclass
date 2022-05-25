# 2022-05-23
# 2022-05-24
import sqlite3
import os

# cur_path = os.path.dirname(__file__)
# conn = sqlite3.connect(cur_path+'/'+'DataBasePM25.sqlite')
conn = sqlite3.connect('DataBasePM25.sqlite')
cursor = conn.cursor()

inputdate = input("請輸入日期(yyyy-mm-dd):")

needcounty = "臺中市"
print("===== 臺中市["+inputdate+"] =====")
cursor = cursor.execute(
    "SELECT InsertNo from TablePM25 ORDER BY InsertNo DESC")
rows = cursor.fetchone()
InsertNo = int(rows[0])

likeinputdate = inputdate+"%"
cursor = cursor.execute(
    "SELECT * from TablePM25 where DataCreationDate LIKE ? AND county=? ORDER BY DataCreationDate", (likeinputdate, needcounty,))
rows = cursor.fetchall()
if(rows == []):
    print('無資料')
else:
    cursor = cursor.execute(
        "SELECT InsertNo from TablePM25 ORDER BY InsertNo DESC")
    rowsno = cursor.fetchone()

    output1 = []
    output2 = []
    areaoutput = [list(range(int(rowsno[0]))) for _ in range(5)]
    areanameoutput = []
    no = 1
    mycount = 0
    smallcount = 0
    for row in rows:
        mycount += 1
        SiteName = row[0]
        PM25 = row[1]
        county = row[2]
        time = row[3]
        time = time[11:]
        insertno = row[4]
        if(mycount < 6):
            areanameoutput.append(SiteName)
        if(no == insertno):
            output1.append(SiteName)
            output2.append(PM25)

            areaoutput[smallcount].append(PM25)
            smallcount += 1

            if(mycount % 5 == 0):
                smallcount = 0
                max = 0
                maxindex = 0
                for i in range(0, 4):
                    if(output2[i] > max):
                        max = output2[i]
                        maxindex = i
                output2[maxindex] = "("+str(output2[maxindex])+")"

                print(time)
                for i in range(0, 5):
                    print("站名:{}  PM2.5={}".format(output1[i], output2[i]))
                output1 = []
                output2 = []
        else:
            no = insertno
            output1.append(SiteName)
            output2.append(PM25)

            areaoutput[smallcount].append(PM25)
            smallcount += 1

    print("===== 臺中市["+inputdate+"] MAX =====")
    for i in range(0, 5):
        areaoutput[i].sort(reverse=True)
        PM25 = areaoutput[i][0]
        if(PM25 < 36):
            color = '綠'
        elif(PM25 < 53):
            color = '黃'
        elif(PM25 < 71):
            color = '紅'
        elif(PM25 >= 71):
            color = '紫'
        print(
            "站名:{}  PM2.5={}  ***{}***".format(areanameoutput[i], PM25, color))

    conn.close()
