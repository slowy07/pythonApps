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

        if len(str(phone_number)) != 12:
            m1 = tk.label(window, text = "Error : please enter 12 digits of number ", fg = 'red', bg = 'black')
            
            canvas_1.create_window(250, 200,  window = m1)
            m1.after(5000, m1.destroy)
            
        else:
            phone_number = [phone_number]
            driver = webdriver.Chrome(executable_path = 'chromedriver', options = option)
            driver.get("https://web.whatsapp.com")
            sleep(15)

            def element_presence(driver, by, xpath, time):
                element_present = EC.presence_of_all_elements_located(By.XPATH, xpath)
                WebDriverWait(driver, time).until(element_present)

            def is_connected():
                try:
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()

            def send_whatsapp_message(driver, phone_no, text, no):
                sleep(5)
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
                
                try:
                    sleep(7)
                    element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    for x in range(no):
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")
                
                except Exception as e:
                    print("invalid Phone number :"+str(phone_no))
            
            for mobile_no in phone_number:
                try:
                    sleep(5)
                    send_whatsapp_message(driver, mobile_no, message_text, no_of_message)
                
                except Exception as e:
                    sleep(10)
                    is_connected()
    
    c1 = tk.Button(text = 'send', command = Driver, bg = 'blue', fg = 'white', font = ('helvetica', 9, 'bold'))
    canvas_1.create_window(250, 380, window = c1)

def orange_selection(event = None):
    with open('birthdays.json') as json_file:
        data = json.load(json_file)
    
    l1 = tk.Label(window, text = "Enter message", bg = 'orange')
    l2 = tk.Label(window, text = "Enter birth month", bg = 'orange')
    l3 = tk.Label(Window, text = "Enter Birth day (2 digits)", bg = 'orange')
    l4 = tk.Label(window, text = "Enter phone number", bg = 'orange')

    h1 = tk.Entry(window)
    h2 = tk.Entry(window)
    h3 = tk.Entry(window)
    h4 = tk.Entry(window)

    canvas_1.create_window(400, 250, window = h1)
    canvas_1.create_window(400, 290, window = h2)
    canvas_1.create_window(400, 300, window = h3)
    canvas_1.create_window(400, 370, window = h4)

    def Driver():
        for p in data:
            if int(p['birth_month']) == now.strftime("%m") and int(p['birth_day']) == now.strftime("%d"):
                driver = webdriver.chrome(executable_path = './chromedriver', options = options)
                sleep(15)
        
        def element_presence(driver, by, xpath, time):
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            WebDriverWait(driver, time).until(element_present)

        def is_connected():
            try:
                # connect to the host -- tells us if the host is actually
                # reachable
                socket.create_connection(("www.google.com", 80))
                return True
            except:
                is_connected()
        
        def send_whatsapp_msg(driver, phone_no):
            sleep(5)
            driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

            try:
                sleep(7)
                element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                for m in data:
                    txt_box.send_keys(m['message_text'])
                    txt_box.send_keys("\n")
            except Exception as e:
                print("Invalid Phone Number:" + str(phone_no))

        for mobile_no in data:
            try:
                print(mobile_no['birth_month'])
                driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
                if mobile_no['birth_month'] == now.strftime("%m") and mobile_no['birth_day'] == now.strftime("%d"):
                    mobile_no = mobile_no['no']
                    print(mobile_no)
                sleep(5)
                send_whatsapp_msg(driver, mobile_no)

            except Exception as e:
                sleep(10)
                is_connected()    

    
    def Add():
        import json
        data = {}
        data1 = []

        message_text = h1.get()
        birth_month = h2.get()
        birth_day = h3.get()

        if len(message_text) == 0 or len(birth_day) == 0 or len(birth_month) == 0:
            m1 = tk.Label(window, text = "Error : fill the blank ", fg = 'red', bg = 'black')
            canvas_1.create_window(250, 140, window = m1)
            m1.after(5000, m1.destroy)

window.mainloop()