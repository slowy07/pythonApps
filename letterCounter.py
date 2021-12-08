# simple letter counter
import tkinter as tk

frameWindow = tk()
frameWindow.geometry("400x260+50+50")
frameWindow.title("simple letter counter")

message1 = tk.StringVar()
letter1 = tk.StringVar()


def printMessage():
    message = message1.get()
    letter = letter1.get()
    message = message.lower()
    letter = letter.lower()

    letterCount = message.count(letter)
    a = "your message have : " + str(letterCount) + " " + letter + "'s in it."
    labelFrameWindow = tk.Label(
        frameWindow, text=a, font=("arial", 15), fg="black"
    ).place(x=10, y=10)
    labelTextField = tk.Label(
        frameWindow,
        text="Enter the letter you want to count",
        font=("ubuntu", 15),
        fg="black",
    ).place(x=10, y=80)
    textField1 = tk.Entry(
        frameWindow, font=("arial", 15), textVariable=message1, bg="white", fg="black"
    ).place(x=10, y=40, height=40, width=340)
    textField2 = tk.Entry(
        frameWindow, font=("arial", 15), textVariable=letter1, bg="white", fg="black"
    ).place(x=10, y=120, height=40, width=340)
    buttonCount = tk.Button(
        frameWindow,
        text="Check letter",
        command=printMessage,
        cursor="hand2",
        font=("Times new roman", 30),
        fg="white",
        bg="black",
    ).place(x=10, y=170, height=40, width=380)

    # print("In this app, I will count the number of times that a specific letter occurs in a message.")
    # message = input("\nPlease enter a message: ")
    # letter = input("Which letter would you like to count the occurrences of?: ")

    frameWindow.mainloop()
