import sqlite3
conn = sqlite3.connect('test.sqlite')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS table01("num"INTEGER PRIMARY KEY NOT NULL,"tel" TEXT)'
cursor.execute(sqlstr)

sqlstr = 'insert into table01 values(1,"02-5555555")'
cursor.execute(sqlstr)
sqlstr = 'insert into table01 values(2,"02-7777777")'
cursor.execute(sqlstr)
sqlstr = 'insert into table01 values(3,"02-5555555")'
cursor.execute(sqlstr)
print('Added 3 records.')
conn.commit()
conn.close()
