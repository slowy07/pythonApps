from __future__ import print_function
import math




key = int(math.pi * 1e14)
text = input("Enter text : ")
values = reverse = []

def encryptChar(target):
    #algorithm
    target = (((target + 449 ) / key) - 449)
    return target

def decryptChar(target):
    target = (((target + 449) / key) - 42)
    return target

def encrypt(inputText):
    colValues = []
    for inp in inputText:
        current = ord(inp)
        current = encryptChar(current)
        colValues.append(current)

    return colValues

def readAndDecrypt(filename):
    file = open(filename, "r")
    data = file.read()
    dataListInt = []
    actualData = []
    dataList = data.split(" ")
    dataList.remove(' ')
    dataListInt = [float(data) for data in dataList]
    for data in dataList:
        current1 = int(decryptChar(data))
        current1 = chr(current1)
        actualData.append(current1)

