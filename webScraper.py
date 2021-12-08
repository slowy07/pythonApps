import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


url = """url to scrapping"""
driver = webdriver.Chrome("./chromedriver")
driver.get(url)
time.sleep(5)


htmlWeb = driver.page_source
soup = BeautifulSoup(htmlWeb, "html.parser")
allInformation = soup.find("div", {"id": "namesearch"})
result = allInformation.find_all("a")

count = 0
for results in result:
    print(results.text)
    count = count + 1
    if count == 10:
        break

driver.close()
