# simple database mysql using python
import mysql.connector

database = mysql.connector.connect(
    host="0.0.0.0", user="root", password="", databaseName="myDatabase"
)
setCursor = database.cursor()
setCursor.execute("SELECT column FROM table")

getResult = setCursor.fetchall()

for x in getResult:
    print(x)
