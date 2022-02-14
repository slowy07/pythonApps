import sqlite3
import time
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image

right = Tk()

right.title("Airline Management System")

right.geometry("570x230")


one = Frame(right, bg="#ED1B24", width=60, height=450)
one.pack(side=LEFT)

two = Frame(right, bg="#1B1464", width=700, height=40)
two.pack(side=TOP)

img = PhotoImage(file="logo.png")
lbl1 = Label(one, image=img, bg="#ED1B24")
lbl1.place(x=50, y=15, anchor=NE)

# lables

lbl1 = Label(two, text="Boarding Pass", font=(" ", 13), fg="#fff", bg="#1B1464")
lbl1.place(x=305, y=6, anchor=NE)

lbl2 = Label(right, text="Passenger Name", font=(" ", 9))
lbl2.place(x=210, y=45, anchor=NE)
lbl3 = Label(right, text="Arfy slowy", font=(" ", 13))
lbl3.place(x=230, y=70, width=140, anchor=NE)

lbl4 = Label(right, text="From", font=(" ", 9))
lbl4.place(x=140, y=110, anchor=NE)
lbl5 = Label(right, text="BOM", font=(" ", 9))
lbl5.place(x=145, y=130, width=50, anchor=NE)

lbl6 = Label(right, text="To", font=(" ", 9))
lbl6.place(x=125, y=160, anchor=NE)
lbl7 = Label(right, text="EWR", font=(" ", 9))
lbl7.place(x=145, y=180, width=50, anchor=NE)

lbl8 = Label(right, text="Flight", font=(" ", 9))
lbl8.place(x=290, y=110, anchor=NE)
lbl9 = Label(right, text="AI 191", font=(" ", 13))
lbl9.place(x=305, y=130, width=50, anchor=NE)

lbl10 = Label(right, text="Date", font=(" ", 9))
lbl10.place(x=370, y=110, anchor=NE)
lbl11 = Label(right, text="28/10/2018", font=(" ", 13))
lbl11.place(x=430, y=130, width=100, anchor=NE)

lbl12 = Label(right, text="Time", font=(" ", 9))
lbl12.place(x=370, y=160, anchor=NE)
lbl13 = Label(right, text="1:44 am", font=(" ", 13))
lbl13.place(x=417, y=180, width=100, anchor=NE)


right.mainloop()
