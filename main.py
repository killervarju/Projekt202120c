from getpass import getpass
import mysql.connector
import os
import time

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="test"
)

clear = lambda: os.system('cls')
login_usname_disp = mydb.cursor()
login_pass_disp = mydb.cursor()

def kezdo():
    print("Logged in!")
    print("Használható parancsok: exit, accountinfo")
    action = input("Adja meg, mit szeretne tenni következőnek: ")
    if action == 'exit' or 'ex':
        print("Kijelentkezés...")
        time.sleep(1)
        print("Kijelentkezve")
        clear()
        login()
    else:
        print("Ismeretlen utasítás!")
        kezdo()


def login():
    print("Login")
    print("--------------------")
    usname = input("Felhasználónév: ")
    pass_word = getpass("Jelszó: ")
    login_usname = """SELECT username FROM users WHERE username = %s"""
    login_usname_disp.execute(login_usname, (usname, ))
    login_usname_disp_result = login_usname_disp.fetchall() 
    login_pass = """SELECT password FROM users WHERE username = %s"""
    login_pass_disp.execute(login_pass, (usname, ))
    login_pass_disp_result = login_usname_disp.fetchall()
    print(login_pass_disp_result)
    print(login_usname_disp_result)
    if  usname == login_usname_disp_result and pass_word == login_pass_disp_result:
        clear()
        kezdo()
    else:
        print("Hibás felhasználónév vagy jelszó!")
        login()
        

if (mydb):
    login()      
else:
    print("ERROR")


'''
login_usname = """SELECT username FROM users WHERE username = %s"""
login_usname_disp.execute(login_usname, (usname, ))
login_usname_disp_result = login_usname_disp.fetchall() 
login_pass = """SELECT password FROM users WHERE username = %s"""
login_pass_disp.execute(login_pass, (usname, ))


--------------------------------------------------------------------
login_usname = """SELECT username FROM users WHERE username = %s"""
mycursor.execute(login_usname, (usname, )) 
login_pass = """SELECT password FROM users WHERE username = %s"""
mycursor.execute(login_pass, (usname, ))

--------------------------------------------------------------------
login_usname = """SELECT username FROM users WHERE username = '%s'""" % (usname)
login_pass = """SELECT password FROM users WHERE username = '%s'""" % (usname)

--------------------------------------------------------------------
login_usname = "SELECT username FROM users WHERE username = '{usname}'" 
login_pass = "SELECT password FROM users WHERE username = '{usname}'" 
'''