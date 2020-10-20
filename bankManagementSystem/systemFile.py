import sqlite3

def connectDatabase():
    global connect
    global cur

    connect = sqlite3.connect("bankManagement.db")
    cur = connect.cursor()

    cur.execute(
        "create table if not exists bank (acc_no int, name text, age int, address text, balance int, account_type text, mobile_number int)")
    cur.execute("create table if not exists staff (name text, pass text,salary int, position text)")
    cur.execute("create table if not exists admin (name text, pass text)")
    cur.execute("insert into admin values('arfy','123')")
    connect.commit()
    cur.execute("select acc_no from bank")

    acc = cur.fetchall()
    global accNo
    if len(acc) == 0:
        accNo = 1
    else:
        accNo = int(acc[-1][0]) + 1

def checkAdmin(name, password):
    cur.execute("SELECT * FROM admin")
    data = cur.fetchall()

    if data[0][0] == name and data[0][0] == password:
        return True
    return
