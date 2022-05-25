import sqlite3
import os
import platform
import urllib.request

from numpy import choose
urllib.request.urlretrieve(
    'http://www1.pu.edu.tw/~yrjean/Sqlite01.txt', 'Sqlite01.sqlite')

con = sqlite3.connect('Sqlite01.sqlite')
cur = con.cursor()


def menu():
    print("========================")
    print("帳密管理系統")
    print("-------------------------")
    print("1. 新增帳號")
    print("2. 顯示帳號")
    print("3. 修改密碼")
    print("4. 刪除帳號")
    print("0. 結束程式")
    print("-------------------------")


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def add():
    while True:
        name = input("請輸入要新增的帳號(Enter==>停止輸入)")
        if(name == ''):
            clear()
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row == None):
                pas = ''
                while(pas == ''):
                    pas = input("請輸入密碼:")
                cur.execute(
                    "INSERT into password values(?,?)", (name, pas))
                con.commit()
                input("帳號新增完畢,請按 ENTER 返回主選單")
                return

            else:
                print(name+" 帳號已存在!")


def show():

    print("帳號\t密碼")
    print("--------------")
    rows = cur.execute('SELECT * FROM password').fetchall()
    for row in rows:
        print("{}\t{}".format(row[0], row[1]))
    print("--------------")
    input("按 ENTER 返回主選單")
    clear()


def edit():
    while True:
        name = input("請輸入要修改的帳號(Enter==>停止輸入)")
        if(name == ''):
            clear()
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row != None):
                print("原來密碼為:"+row[1])
                newpas = input("請輸入新密碼:")
                cur.execute(
                    "UPDATE password set pass=? where name=?", (newpas, name))
                con.commit()
                input("密碼更改完畢,請按 ENTER 返回主選單")
                return

            else:
                print(name+" 帳號不存在!")


def delete():
    while True:
        name = input("請輸入要刪除的帳號(Enter==>停止輸入)")
        if(name == ''):
            clear()
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row != None):
                ans = input("確定刪除"+name+"的資料(Y/N)?")
                if(ans == 'y' or ans == 'Y'):
                    cur.execute(
                        "Delete From password WHERE name=?", (name,))
                    con.commit()
                    input("帳號刪除完畢,請按 ENTER 返回主選單")
                    return
            else:
                print(name+"帳號不存在!")


switch = {1: add, 2: show, 3: edit, 4: delete}
while True:
    menu()
    choose = int(input("請輸入您的選擇 : "))
    print()
    if(choose != 0):
        switch.get(choose, exit)()
    else:
        print("程式執行完畢!")
        exit()
