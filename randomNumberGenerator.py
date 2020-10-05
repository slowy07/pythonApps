from random import randint
from tkinter import *

def rollDice():
    text.delete(0.0, END)
    text.insert(END,  str(randint(1,100)))

FrameWindow = Tk()
text = Text(FrameWindow, width=3, height=1)
buttonGenerate = Button(FrameWindow, text="Press to Roll !", command=rollDice)
text.pack()
buttonGenerate.pack()
FrameWindow.mainloop()

