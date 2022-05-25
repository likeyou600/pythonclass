import sqlite3
conn =sqlite3.connect('test.sqlite') #建立資料庫連線，若不存在，會先新增資料庫

cursor =conn.execute('select * from table01')
rows=cursor.fetchall()

print(rows)
for row in rows:
    print(type(row))
    print("{}\t{}".format(row[0], row[1]))

print("--------------")
cursor =conn.execute('select count(*) from table01')
row =cursor.fetchone()

print(row)
print(type(row))
print('%d records in table01'%row[0])
conn.close()#關閉資料連線 對(DATABASE)>>conn