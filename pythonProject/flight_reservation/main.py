import os.path
import sqlite3
import time
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image

# main screen
root = Tk()
root.title("Title")
root.geometry("720x565")
root.geometry("+300+100")

style = ttk.Style(root)

right = Frame(root, width=1500, height=565)
right.pack(side=LEFT)

# databse name
db_name = "C:/Users/DELL/Desktop/DBMS/airline.db"

# database query
def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        query_result = cursor.execute(query, parameters)
        conn.commit()
    return query_result


# messagebox for add
def clk_add1():
    messagebox.showinfo(" ", "Data Added Successfully !")


def clk_add2():
    messagebox.showinfo(" ", "Fields Are Empty")


# validation
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


# lables

lbl1 = Label(right, text="PID.")
lbl1.place(x=50, y=0, anchor=NE)
txt1 = Entry(right, width=11)
txt1.place(x=200, y=3, anchor=NE)

lbl2 = Label(right, text="Name")
lbl2.place(x=55, y=50, anchor=NE)
txt2 = Entry(right, width=20)
txt2.place(x=230, y=50, anchor=NE)

lbl3 = Label(right, text="Age")
lbl3.place(x=50, y=100, anchor=NE)
txt3 = Entry(right, width=5)
txt3.place(x=180, y=100, anchor=NE)

lbl4 = Label(right, text="Sex")
lbl4.place(x=45, y=150, anchor=NE)
txt4 = Entry(right, width=5)
txt4.place(x=180, y=150, anchor=NE)

lbl5 = Label(right, text="Address")
lbl5.place(x=60, y=200, anchor=NE)
txt5 = Entry(right, width=20)
txt5.place(x=230, y=200, anchor=NE)

lbl6 = Label(right, text="Contact")
lbl6.place(x=60, y=250, anchor=NE)
txt6 = Entry(right, width=20)
txt6.place(x=230, y=250, anchor=NE)

lbl7 = Label(right, text="Email")
lbl7.place(x=55, y=300, anchor=NE)
txt7 = Entry(right, width=20)
txt7.place(x=230, y=300, anchor=NE)

# buttons
btn1 = Button(right, text="Add Data", command=adding)
btn1.place(x=100, y=350, anchor=NE)

root.mainloop()
