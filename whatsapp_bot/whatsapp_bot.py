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





window.mainloop()