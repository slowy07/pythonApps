import tkinter.messagebox
from tkinter import *
import systemFile

systemFile.connectDatabase()

def checkStringInAccountNo(checkAccNo):
    r = checkAccNo.isDigit()
    return r

def create():
    def createCustomerInDatabase():
        def deleteCreate():
            createEmployeeFrame.grirdForget()
            page2()

        name = entry5.get()
        age = entry6.get()
        address = entry7.get()
        balance = entry8.get()
        accType = entry9.get()
        mobileNumber = entry10.get()
        if len(name) != 0 and len(age) != 0 and len(address) != 0 and len(balance) != 0 and len(accType) != 0 and len(mobileNumber) != 0:
            accNo = systemFile.createCustomer(name, age, address, balance, accType, mobileNumber)
            global accNo
            cur.execute("INSERT INTO bank VALUES(?,?,?,?,?,?,?)", (accNo, name, age, addres, balance, accType, mobileNumber))
            connect.commit()
            accNo = accNo + 1
