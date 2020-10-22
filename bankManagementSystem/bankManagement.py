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
            createEmployeeFrame.grid_forget()
            page2()

        name = entry5.get()
        age = entry6.get()
        address = entry7.get()
        balance = entry8.get()
        accType = entry9.get()
        mobileNumber = entry10.get()
        if len(name) != 0 and len(age) != 0 and len(address) != 0 and len(balance) != 0 and len(accType) != 0 and len(mobileNumber) != 0:
            accNo = systemFile.createCustomer(name, age, address, balance, accType, mobileNumber)
            label = Label(createEmployeeFrame, text='your account number is {}'.format(accNo))
            label.grid(row=14)

            button = Button(createEmployeeFrame, text='exit', command=deleteCreate)
            button.grid(row=25)
        else:
            label = Label(createEmployeeFrame, text='please fill all entries')
            label.grid(row = 14)

            button = Button(createEmployeeFrame, text='exit', command=deleteCreate)
            button.grid(row=15)

          frame1.grid_forget()
    global createEmployeeFrame
    createEmployeeFrame = Frame(tk, bg='black')
    createEmployeeFrame.grid(padx=500, pady=150)

    label = Label(createEmployeeFrame, text='Customer Detail', font='bold')
    label.grid(row=0, pady=4)
    label = Label(createEmployeeFrame, text='Name', font='bold')
    label.grid(row=1, pady=4)
    global entry5
    entry5 = Entry(createEmployeeFrame)
    entry5.grid(row=2, pady=4)
    label = Label(createEmployeeFrame, text='Age', font='bold')
    label.grid(row=3, pady=4)
    global entry6
    entry6 = Entry(createEmployeeFrame)
    entry6.grid(row=4, pady=4)
    label = Label(createEmployeeFrame, text='address', font='bold')
    label.grid(row=5, pady=4)
    global entry7
    entry7 = Entry(createEmployeeFrame)
    entry7.grid(row=6, pady=4)
    label = Label(createEmployeeFrame, text='Balance', font='bold')
    label.grid(row=7, pady=4)
    global entry8
    entry8 = Entry(createEmployeeFrame)
    entry8.grid(row=8, pady=4)
    label = Label(createEmployeeFrame, text='Account Type', font='bold')
    label.grid(row=9, pady=4)
    label = Label(createEmployeeFrame, text='Mobile number', font='bold')
    label.grid(row=11, pady=4)
    global entry9
    entry9 = Entry(createEmployeeFrame)
    entry9.grid(row=10, pady=4)
    global entry10
    entry10 = Entry(createEmployeeFrame)
    entry10.grid(row=12, pady=4)
    button = Button(createEmployeeFrame, text='Submit', command=createCustomerInDatabase)
    button.grid(row=13, pady=4)

    mainloop()

def searchAcc():
    frame1.grid_forget()
    global searchFrame
    searchFrame = Frame(tk)
    searchFrame.grid(padx=500, pady=300)

    label = Label(searchFrame, text='enter account number', font='bold')
    label.grid(row=0, pady=6)
    global entry11
    entry11 = Entry(searchFrame)
    entry.grid(row=1, pady=6)

    button = Button(searchFrame, text='search acc', command=show)

    mainloop()

def show():
    def clearShowFrame():
        showFrame.grid_forget()
        page2()
    def backPage2():
        searchFrame.grid_forget()
        page2()

    accNo = entry11.get()
    r = checkStringInAccountNo(accNo)
    if len(accNo) != 0 and r:
        details = systemFile.getDetails(accNo)
        if details != False:
            searchFrame.grid_forget()
            global showFrame
            showFrame = Frame(tk)
            showFrame.grid(padx=400, pady=200)

            label = Label(showFrame, text="Account_number:\t{}".format(details[0]), font='bold')
            label.grid(row=0, pady=6)
            label = Label(showFrame, text="Name:\t{}".format(details[1]), font='bold')
            label.grid(row=1, pady=6)
            label = Label(showFrame, text="Age:\t{}".format(details[2]), font='bold')
            label.grid(row=2, pady=6)
            label = Label(showFrame, text="Address:\t{}".format(details[3]), font='bold')
            label.grid(row=3, pady=6)
            label = Label(showFrame, text="Balance:\t{}".format(details[4]), font='bold')
            label.grid(row=4, pady=6)
            label = Label(showFrame, text="Account_type:\t{}".format(details[5]), font='bold')
            label.grid(row=5, pady=6)
            label = Label(showFrame, text="Mobile Number:\t{}".format(details[6]), font='bold')
            label.grid(row=6, pady=6)
            button = Button(showFrame, text='Exit', command=clearShowFrame, width=20, height=2, bg='red', fg='white')
            button.grid(row=7, pady=6)
            mainloop()

        else:
            label = Label(searchFrame, text='account not found')
            label.grid()
            button = Label(searchFrame, text='exit', command=backPage2)
            button.grid()
    else:
        label = Label(searchFrame, text='Enter correct account number')
        label.grid()
        button = Button(searchFrame, text='exit', command=backPage2)
        button.grid()

def add():
    frame1.grid_forget()
    def searchInDatabase():
        def backPage2():
            searchFrame.grid_forget()
            page2()

        global result
        global accNo
        accNo = entry11.get()
        r = checkStringInAccountNo(accNo)
        if len(accNo) != 0 and r:
            result = systemFile.checkAccNo(accNo)
            print(result)
            if not result:
                label = Label(searchFrame, text='invalid account number')
                lable.grid(pady=2)
                button = Button(searchFrame, text='exit', command=backPage2)
                button.grid()
                mainloop()
            else:
                def updateMoney():
                    newMoney = entry12.get()
                    systemFile.updateBalance(newMoney, accNo)
                    addFrame.grid_forget()
                    page2()

                searchFrame.grid_forget()
                global addFrame
                addFrame = Frame(tk)
                addFrame.grid(pady=400, paddy=300)

                detail = systemFile.getDetail(accNo)
                label = Label(addFrame, text='account holder name :  {} '.format(detail[0][0]))
                label.grid(row=0, pady=3)

                label = Label(addFrame, text='current amount :  {}'.format(detail[0][1]))
                label.grid(row=1, pady=3)

                label = Label(addFrame, text='enter money')
                label.grid(row=2, pady=3)
                global entry12
                entry12 = Entry(addFrame)
                entry12.grid(row=3, pady=3)

                button = Button(addFrame, text='add', command=updateMoney)
                button.grid(row=4)

                mainloop()
                 
