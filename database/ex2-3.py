import sqlite3
conn = sqlite3.connect('test.sqlite')


def print_table01():
    cursor = conn.execute('select * from table01')
    rows = cursor.fetchall()
    for row in rows:
        print("{}\t{}".format(row[0], row[1]))
    print("================")


print("-------原始資料表------")
print_table01()
print("-------新增一筆紀錄------")
sqlstr = 'insert into table01 values(4,"04-7654321")'
conn.execute(sqlstr)
print_table01()

print("-------變更一筆紀錄------")
sqlstr = 'update table01 set tel="02-8888888" where num=4'
conn.execute(sqlstr)
print_table01()
print("-------刪除一筆紀錄------")
sqlstr = 'delete from table01 where num=4'
conn.execute(sqlstr)
print_table01()

conn.commit()
conn.close()
