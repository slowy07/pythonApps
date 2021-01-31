import socket
import tkinter as tk
from datetime import datetime
from time import sleep
import time 
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


now = datetime.now()
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=./User_Data')

window = tk.Tk()
window.title('whatsapp bot')
width = 500
height = 700

canvas_1 = tk.Canvas(window, width = width, height = height, relief = 'raised', bg = 'white')
canvas_1.pack()

canvas_1.create_line(width / 2, 0, width / 2, height, dash = (4,2))
canvas_1.create_line(800, height / 2, 0, height / 2, dash = (4,2))

cx = canvas_1.canvasx(width / 2)
cy = canvas_1.canvasy(height / 2)

cid = canvas_1.find_closest(cx, cy)[0]
canvas_1.itemconfigure(cid, fill="blue")

image_data = tk.PhotoImage(file = 'image_data.png')
canvas_1.create_image(width / 2, height / 2, image = image_data)

def blue_selection(event = None):
    l1 = tk.Label(window, text = 'Enter message', bg='blue')
    l2 = tk.Label(window, text = 'How many message you want to send', bg = 'blue')
    l3 = tk.Label(window, text = 'Enter phone number', blue = 'blue')

    canvas_1.create_window(100, 250, window = l1)
    canvas_1.create_window(150, 290, window = l2)
    canvas_1.create_window(100, 300, window = l3)

    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)

    canvas_1.create_window(400, 250, window = e1)
    canvas_1.create_window(400, 290, window = e2)
    canvas_1.create_window(400, 330, window = e3)

    def Driver():
        message_text = e1.get()
        no_of_message = e2.get()
        if type(no_of_message) == int:
            print("Number is integer "+str(no_of_message))
        else:
            try:
                no_of_message = int(no_of_message)
            except:
                m1 = tk.Label(window, text = "Error: please enter digits of message ", fg = 'red', bg = 'black')

            canvas_1.create_window(250, 170, window = m1)
            m1.after(5000, m1.destroy)
        
        if len(message_text) == 0 or len(str(no_of_message)) == 0:
            m1 = tk.Label(window, text = "Error: please enter 12 digits of phone number ", fg = 'red', bg = 'black')
            canvas_1.create_window(250, 140, window = m1)
            m1.after(5000, m1.destroy)

        phone_number = int(e3.get())


window.mainloop()