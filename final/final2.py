import sqlite3
import os
import platform
import urllib.request
import readchar


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
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row == None):
                pas = ''
                repeatpas = ''
                repeatpascheck = False
                while(repeatpascheck == False):
                    pas = input("請輸入新密碼:")
                    if(pas != ''):
                        repeatpas = input("請再次輸入新密碼:")
                        while(pas != repeatpas):
                            print("密碼不相同，重新輸入")
                            repeatpas = input("請再次輸入新密碼:")
                        repeatpascheck = True

                cur.execute(
                    "INSERT into password values(?,?)", (name, pas))
                con.commit()
                print("帳號新增完畢,請按任意鍵返回主選單")
                readchar.readchar()

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
    print("按任意鍵返回主選單")
    readchar.readchar()





def edit():
    while True:
        name = input("請輸入要修改的帳號(Enter==>停止輸入)")
        if(name == ''):
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row != None):
                oldpas = input("請輸入原密碼:")
                if(row[1]!=oldpas):
                    print("密碼錯誤，無法修改")
                else:
                    
                    pas = ''
                    repeatpas = ''
                    repeatpascheck = False
                    while(repeatpascheck == False):
                        pas = input("請輸入新密碼:")
                        if(pas != ''):
                            repeatpas = input("請再次輸入新密碼:")
                            while(pas != repeatpas):
                                print("密碼不相同，重新輸入")
                                repeatpas = input("請再次輸入新密碼:")
                            repeatpascheck = True


                    cur.execute(
                        "UPDATE password set pass=? where name=?", (pas, name))
                    con.commit()
                    
                    print("密碼更改完畢,請按任意鍵返回主選單")
                    readchar.readchar()
                    return

            else:
                print(name+" 帳號不存在!")


def delete():
    while True:
        name = input("請輸入要刪除的帳號(Enter==>停止輸入)")
        if(name == ''):
            return
        else:
            row = cur.execute(
                "SELECT * FROM password WHERE name = ?", (name,)).fetchone()
            if(row != None):
                oldpas = input("請輸入原密碼:")
                if(row[1]!=oldpas):
                    print("密碼錯誤，無法刪除")
                else:
                    ans = input("確定刪除"+name+"的資料(Y/N)?")
                    if(ans == 'y' or ans == 'Y'):
                        cur.execute(
                            "Delete From password WHERE name=?", (name,))
                        con.commit()
                        print("帳號刪除完畢,請按任意鍵返回主選單")
                        readchar.readchar()
                        return
            else:
                print(name+"帳號不存在!")


switch = {1: add, 2: show, 3: edit, 4: delete}
while True:
    clear()
    menu()
    chooses = int(input("請輸入您的選擇 : "))
    print()
    if(chooses != 0):
        switch.get(chooses, exit)()
    else:
        print("程式執行完畢!")
        exit()
