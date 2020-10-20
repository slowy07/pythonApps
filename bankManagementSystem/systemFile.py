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

def createEmployee(name, password, salary, position):
    print(password)
    cur.execute("INSERT INTO staff VALUES(?,?,?,?)",(name, password, salary, position))
    connect.commit()

def checkEmployee(name, password):
    print(password)
    print(name)
    cur.execute("SELECT * name, pass FROM staff")
    data = cur.fetchall()
    print(data)
    if len(data) == 0:
        return False
    for i in range(len(data)):
        if data[i][0] == name and data[i][1] == password:
            return True

    return False

def createCustomer(name, age, address, balance, accType, mobileNumber):
        global accNo
        cur.execute("INSERT INTO bank VALUES(?,?,?,?,?,?,?)", (accNo, name, age, address, balance, accType, mobileNumber))
        connect.commit()
        accNo = accNo + 1

        return accNo + 1


def checkAccNo(accNo):
    cur.execute("SELECT acc_no FROM bank")
    listAccNo = cur.fetchall()

    for i in range(len(listAccNo)):
        if listAccNo[i][0] == int(accNo):
            return True

    return False

def getDetails(accNo):
    cur.execute("SELECT * FROM bank WHERE acc_no=?",(accNo))
    global detail
    detail = cur.fetchall()
    print(detail)
    if len(detail) == 0:
        return False
    else:
        return (detail[0][0], detail[0][1], detail[0][2], detail[0][3], detail[0][4], detail[0][5], detail[0][6])

def updateBalance(newMoney, accNo):
    cur.execute("SELECT balance FROM bank WHERE acc_no=?",(accNo))
    balance = cur.fetchall()
    balance = balance[0][0]
    newBalance = balance + int(newMoney)
    cur.execute("UPDATE bank SET balance=? WHERE acc_no =?",(newBalance, accNo))
    connect.commit()

def deductBalance(newMoney, accNo):
    cur.execute("SELECT balance FROM bank WHERE acc_no = ?",(accNo))
    balance = cur.fetchall()
    balance = balance[0][0]
    if balance < int(newMoney):
        return False
    else:
        newBalance = balance - int(newMoney)
        cur.execute("UPDATE bank SET balance=? WHERE acc_no =?",(newBalance, accNo))
        connect.commit()
        return True


def checkBalance(accNo):
    cur.execute("SELECT balance FROM bank WHERE acc_no=?", (accNo))
    balance = cur.fetchall()
    return balance[0][0]

def updateNameInBankTable(newName, accNo):
    print(newName)
    connect.excecute("UPDATE bank SET name='{}' WHERE acc_no={}".format(newName, accNo))
    connect.commit()

def updateAgeInBankTable(newAge, accNo):
    print(newAge)
    connect.excecute("UPDATE bank SET age='{}' WHERE acc_no={}".format(newAge, accNo))
    connect.commit()

def updateAddressInBankTable(newAddress, accNo):
    print(newAddress)
    connect.excecute("UPDATE bank SET address='{}' WHERE acc_no={}".format(newAddress, accNo))
    connect.commit()

def listAllCustomer():
    cur.execute("SELECT * FROM bank")
    detail = cur.fetchall()
    return detail

def deleteAccount(accNo):
    cur.execute("DELETE FROM bank WHERE acc_no=?",(accNo))
    connect.commit()

def showEmployees():
    cur.execute("SELECT name, salary, position, pass FROM staff")
    detail = cur.fetchall()
    return detail

def allMoney():
    cur.execut("SELECT balance FROM bank")
    balanceDetail = cur.fetchall()
    print(balanceDetail)
    if len(balanceDetail) == 0:
        return False
    else:
        total = 0
        for i in balanceDetail:
            total = total + i[0]
        return total

def showEmployeesForUpdate():
    cur.execute("SELECT * FROM staff")
    detail = cur.fetchall()
    return detail

def update_employee_name(newName, oldName):
    print(newName, oldName)
    cur.execute("update staff set name='{}' where name='{}'".format(newName, oldName))
    connect.commit()


def update_employee_password(newPass, oldName):
    print(newPass, oldName)
    cur.execute("update staff set pass='{}' where name='{}'".format(newPass, oldName))
    connect.commit()


def update_employee_salary(newSalary, oldName):
    print(newSalary, oldName)
    cur.execute("update staff set salary={} where name='{}'".format(newSalary, oldName))
    connect.commit()


def update_employee_position(newPos, oldName):
    print(newPos, oldName)
    cur.execute("update staff set position='{}' where name='{}'".format(newPos, oldName))
    connect.commit()

def get_detail(accNo):
    cur.execute("select name, balance from bank where acc_no=?", (accNo))
    detail = cur.fetchall()
    return detail

def chekNameInStaff(name):
    cur = connect.cursor()
    cur.execute("SELECT name FROM staff")
    detail = cur.fetchall()

    for i in detail:
        if i[0] == name:
            return True
    return False
