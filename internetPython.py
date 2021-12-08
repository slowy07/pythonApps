from __future__ import print_function
import os
import urllib.request
from selenium import webdriver

print("test internet connection")
print()

try:
    urllib.request.urlopen("https://google.com", timeout=2)
    print("internet works fine !")
    questionOpen = input("open website (y/n) :")
    if questionOpen == "y" and questionOpen == "Y":
        search = input("input website name (http://website.com) :")
    else:
        os._exit(0)
except urllib.error.URLError:
    print("no internet connection")

browser = webdriver.Firefox()  # using Firefox
browser.get(search)
os.system("clear")  # os.system('cls') windows user
print("[+] website " + search + " openend")
browser.close()
