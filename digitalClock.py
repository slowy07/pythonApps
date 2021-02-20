import time
from time import strftime

from tkinter import *
from tkinter.ttk import *

frameWindow = Tk()
frameWindow.title('clock')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(frameWindow, font = ('Calibri', 40, 'bold', 'italic'), bg = 'black', fg='yellow')
label.pack(anchor = 'center')
time()
label1 = Label(frameWindow, font = ('Arial', 30, 'bold'), bg = 'black', fg = 'white', bd = 30)
label1.grid(row = 0, column = 1)

def digitalClock():
    textInput = time.strftime("%H : %M : %S")
    label11.config(text = textInput)
    label1.after(200, digitalClock)

digitalClock()
frameWindow.mainloop()
