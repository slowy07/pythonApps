import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

window = Tk()
window.title("airline management system")
window.geometry("500x450")


def new():
    newwin = Toplevel(window)
    newwin.geometry("650x360")

    def run_query3(query9):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            query_result3 = cursor.execute(query9, (txt15.get(),))
            conn.commit()

        return query_result3

    def viewing_records1():
        records1 = tree1.get_childern()
        for element in records1:
            tree1.delete(element)

        query9 = "SELECT * FROM passenger WHERE pid =?"
        db_rows = run_query(query9)
        for row in db_rows:
            tree1.insert(
                "",
                0,
                text=row[0],
                values=(row[1], row[2], row[3], row[3], row[4], row[5], row[6]),
            )

    tree1 = ttk.Treeview(newwin, height=10, column=6)
    tree1["column"] = ("#0", "#1", "#2", "#3", "#4", "#5")
    tree1.grid(row=0, column=0, columnspan=6, padx=14, pady=15)
    tree1.heading("#0", text="PID")
    tree1.column("#0", anchor="center", width=70)
    tree1.heading("#1", text="Name")
    tree1.column("#1", anchor="center", width=110)
    tree1.heading("#2", text="Age")
    tree1.column("#2", anchor="center", width=60)
    tree1.heading("#3", text="Sex")
    tree1.column("#3", anchor="center", width=80)
    tree1.heading("#4", text="Address")
    tree1.column("#4", anchor="center", width=80)
    tree1.heading("#5", text="Contact")
    tree1.column("#5", anchor="center", width=80)
    tree1.heading("#6", text="Email")
    tree1.column("#6", anchor="center", width=130)

    viewing_records1()


tab_control = ttk.Notebook(window)
right = ttk.Frame(tab_control)
left = ttk.Frame(tab_control)
three = ttk.Frame(tab_control)
four = ttk.Frame(tab_control)

right1 = Frame(three, width=500, height=500)
right1.pack(side=RIGHT)
left1 = Frame(three, width=500, height=500)
left1.pack(side=LEFT)

tab_control.add(right, text="Passenger Info")
tab_control.add(left, text="Airline Info")
tab_control.add(three, text="Book Ticket")
tab_control.add(four, text="Boarding Pass")

db_name = "airline.db"


def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result = cursor.execute(query, parameters)
        conn.commit()
    return query_result


def clk_add1():
    messagebox.showinfo(" ", "Data Added Successfully !")


def clk_add2():
    messagebox.showinfo(" ", "Fields Are Empty")


def validation():
    return len(txt5.get()) != 0


# adding data in database
def adding():
    if validation():

        query = "INSERT INTO passenger VALUES (?, ?, ?, ?, ?, ?, ?)"
        parameters = (
            txt1.get(),
            txt2.get(),
            txt3.get(),
            txt4.get(),
            txt5.get(),
            txt6.get(),
            txt7.get(),
        )
        run_query(query, parameters)
        clk_add1()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)
        txt7.delete(0, END)

    else:
        clk_add2()


lbl1 = Label(right, text="PID.")
lbl1.place(x=50, y=60, anchor=NE)
txt1 = Entry(right, width=11)
txt1.place(x=200, y=60, anchor=NE)

lbl2 = Label(right, text="Name")
lbl2.place(x=300, y=60, anchor=NE)
txt2 = Entry(right, width=20)
txt2.place(x=490, y=60, anchor=NE)

lbl3 = Label(right, text="Age")
lbl3.place(x=50, y=110, anchor=NE)
txt3 = Entry(right, width=5)
txt3.place(x=180, y=110, anchor=NE)

lbl4 = Label(right, text="Sex")
lbl4.place(x=290, y=110, anchor=NE)
txt4 = Entry(right, width=5)
txt4.place(x=450, y=110, anchor=NE)

lbl5 = Label(right, text="Address")
lbl5.place(x=60, y=160, anchor=NE)
txt5 = Entry(right, width=20)
txt5.place(x=220, y=160, anchor=NE)

lbl6 = Label(right, text="Contact")
lbl6.place(x=305, y=160, anchor=NE)
txt6 = Entry(right, width=20)
txt6.place(x=495, y=160, anchor=NE)

lbl7 = Label(right, text="Email")
lbl7.place(x=180, y=210, anchor=NE)
txt7 = Entry(right, width=20)
txt7.place(x=350, y=210, anchor=NE)

# buttons
btn1 = Button(right, text="Add Data", command=adding)
btn1.place(x=300, y=260, anchor=NE)

tab_control.pack(expand=1, fill="both")

# database query
def run_query1(query1, parameters1=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result1 = cursor.execute(query1, parameters1)
        conn.commit()
    return query_result1


# messagebox for add
def clk_flight1():
    messagebox.showinfo(" ", "Data Added Successfully !")


def clk_flight2():
    messagebox.showinfo(" ", "Fields Are Empty")


# validation
def validation1():
    return len(txt14.get()) != 0


# adding data in database
def adding1():
    if validation1():

        query1 = "INSERT INTO flight VALUES (?, ?, ?, ?, ?, ?, ?)"
        parameters1 = (
            txt8.get(),
            txt9.get(),
            txt10.get(),
            txt11.get(),
            txt12.get(),
            txt13.get(),
            txt14.get(),
        )
        run_query1(query1, parameters1)
        clk_flight1()
        txt8.delete(0, END)
        txt9.delete(0, END)
        txt10.delete(0, END)
        txt11.delete(0, END)
        txt12.delete(0, END)
        txt13.delete(0, END)
        txt14.delete(0, END)

    else:
        clk_flight2()


# lables

lbl8 = Label(left, text="Flight No.")
lbl8.place(x=70, y=60, anchor=NE)
txt8 = Entry(left, width=11)
txt8.place(x=200, y=60, anchor=NE)

lbl9 = Label(left, text="From")
lbl9.place(x=300, y=60, anchor=NE)
txt9 = Entry(left, width=20)
txt9.place(x=500, y=60, anchor=NE)

lbl10 = Label(left, text="To")
lbl10.place(x=50, y=110, anchor=NE)
txt10 = Entry(left, width=5)
txt10.place(x=180, y=110, anchor=NE)

lbl11 = Label(left, text="Dep. Date")
lbl11.place(x=320, y=110, anchor=NE)
txt11 = Entry(left, width=5)
txt11.place(x=450, y=110, anchor=NE)

lbl12 = Label(left, text="Dep. Time")
lbl12.place(x=70, y=160, anchor=NE)
txt12 = Entry(left, width=20)
txt12.place(x=230, y=160, anchor=NE)

lbl13 = Label(left, text="Arr. Date")
lbl13.place(x=310, y=160, anchor=NE)
txt13 = Entry(left, width=20)
txt13.place(x=500, y=160, anchor=NE)

lbl14 = Label(left, text="Arr. Time")
lbl14.place(x=200, y=210, anchor=NE)
txt14 = Entry(left, width=20)
txt14.place(x=350, y=210, anchor=NE)

# buttons
btn2 = Button(left, text="Add Data", command=adding1)
btn2.place(x=300, y=260, anchor=NE)


def viewing_records():

    records = tree.get_children()
    for element in records:
        tree.delete(element)
    query = "SELECT * FROM flight ORDER by flight_no DESC"
    db_rows = run_query(query)
    for row in db_rows:
        tree.insert(
            "", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6])
        )


# messagebox for booking
def clk_book():
    messagebox.showinfo(" ", "Ticket Booked Successfully !")


# database query


def run_query2(query2, parameters2=()):
    with sqlite3.connect(db_name) as conn:

        cursor = conn.cursor()
        query_result2 = cursor.execute(query2, parameters2)
        conn.commit()

        clk_book()
    return query_result2


# ticke booking
def adding2():

    data = tree.item(tree.selection())["text"]
    print(data)

    query2 = "INSERT INTO booking (pid, name, age, sex, addr, contact, email, flight_no, frm, too, dep_date, dep_time, arr_date, arr_time) SELECT passenger.* , flight.* FROM passenger, flight WHERE pid = ? AND flight_no = ?"
    parameters2 = (txt15.get(), data)

    run_query2(query2, parameters2)

    txt15.delete(0, END)

    viewing_records()


# lables

lbl15 = Label(three, text="Enter PID.")
lbl15.place(x=230, y=25, anchor=NE)
txt15 = Entry(three, width=11)
txt15.place(x=320, y=25, anchor=NE)


# buttons

btn4 = Button(three, text="Book Flight", command=adding2)
btn4.place(x=300, y=350, anchor=NE)

btn5 = Button(three, text="Get Info", command=new)
btn5.place(x=400, y=20, anchor=NE)

# treeview_flight
tree = ttk.Treeview(right1, height=10, column=6)
tree["column"] = ("#0", "#1", "#2", "#3", "#4", "#5")
tree.grid(row=0, column=0, columnspan=6, padx=14, pady=15)

tree.heading("#0", text="Flight No.")
tree.column("#0", anchor="center", width=70)
tree.heading("#1", text="From")
tree.column("#1", anchor="center", width=60)
tree.heading("#2", text="To")
tree.column("#2", anchor="center", width=60)
tree.heading("#3", text="Dep. Date")
tree.column("#3", anchor="center", width=80)
tree.heading("#4", text="Dep. Time")
tree.column("#4", anchor="center", width=80)
tree.heading("#5", text="Arr. Date")
tree.column("#5", anchor="center", width=80)
tree.heading("#6", text="Arr. Time")
tree.column("#6", anchor="center", width=80)


viewing_records()

# Tab4

# create new window


def new1():  # new window definition
    newwin1 = Toplevel(window)
    newwin1.geometry("570x230")

    one = Frame(newwin1, bg="#ED1B24", width=60, height=450)
    one.pack(side=LEFT)

    two = Frame(newwin1, bg="#1B1464", width=700, height=40)
    two.pack(side=TOP)

    def run_query4(query7, value):
        with sqlite3.connect(db_name) as conn:

            cursor = conn.cursor()
            query_result7 = cursor.execute(query7, (value,))
            conn.commit()
            result = cursor.fetchall()
        return result

    # ticke viewing
    def ticket():

        query7 = "SELECT name, flight_no, frm, too, dep_date, dep_time FROM booking WHERE pid = ?"

        value = txt36.get()

        result = run_query4(query7, value)

        for row in result:

            lbl18.config(text=row[0])
            lbl20.config(text=row[2])
            lbl22.config(text=row[3])
            lbl24.config(text=row[1])
            lbl26.config(text=row[4])
            lbl28.config(text=row[5])

    # Labels

    lbl16 = Label(two, text="Boarding Pass", font=(" ", 13), fg="#fff", bg="#1B1464")
    lbl16.place(x=305, y=6, anchor=NE)

    lbl17 = Label(newwin1, text="Passenger Name", font=(" ", 9))
    lbl17.place(x=210, y=45, anchor=NE)
    lbl18 = Label(newwin1, font=(" ", 13))
    lbl18.place(x=230, y=70, width=140, anchor=NE)

    lbl19 = Label(newwin1, text="From", font=(" ", 9))
    lbl19.place(x=140, y=110, anchor=NE)
    lbl20 = Label(newwin1, font=(" ", 9))
    lbl20.place(x=145, y=130, width=50, anchor=NE)

    lbl21 = Label(newwin1, text="To", font=(" ", 9))
    lbl21.place(x=125, y=160, anchor=NE)
    lbl22 = Label(newwin1, font=(" ", 9))
    lbl22.place(x=145, y=180, width=50, anchor=NE)

    lbl23 = Label(newwin1, text="Flight", font=(" ", 9))
    lbl23.place(x=290, y=110, anchor=NE)
    lbl24 = Label(newwin1, font=(" ", 13))
    lbl24.place(x=305, y=130, width=50, anchor=NE)

    lbl25 = Label(newwin1, text="Date", font=(" ", 9))
    lbl25.place(x=370, y=110, anchor=NE)
    lbl26 = Label(newwin1, font=(" ", 13))
    lbl26.place(x=430, y=130, width=100, anchor=NE)

    lbl27 = Label(newwin1, text="Time", font=(" ", 9))
    lbl27.place(x=370, y=160, anchor=NE)
    lbl28 = Label(newwin1, font=(" ", 13))
    lbl28.place(x=417, y=180, width=100, anchor=NE)

    ticket()

    img = PhotoImage(file="logo.png")
    lbl29 = Label(one, image=img, bg="#ED1B24")
    lbl29.place(x=20, y=15, anchor=NE)


# lables

lbl36 = Label(four, text="Enter PID.")
lbl36.place(x=250, y=150, anchor=NE)
txt36 = Entry(four, width=11)
txt36.place(x=350, y=150, anchor=NE)


# Buttons

btn6 = Button(four, text="Get The Boarding Pass", command=new1)
btn6.place(x=340, y=200, anchor=NE)

window.mainloop()


print("getMsss")


window.mainloop()
