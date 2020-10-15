import cv2
import numpy as np
import math
import colorsys
import pandas as pd
import os
import argparse
from tqdm import tqdm
import sound


parser = argparse.ArgumentParser()
parser.add_argument("-f", required=True, help="Enter filename of your picture : ")
#parser.add_argument("-s", required=True, help="Speed factor of the audio to be increased or decreased")
#parser.add_argument("-av", required=True, help="Speed factor of the audio visualizer to be increased or decreased")

args = parser.parse_args()
os.makedirs("Image_sort/"+str(args.f))
print(str(args.f).capitalize()+" directory is created!")

df =[]
total = 0
dict, final, imgList = {}, [], []

def createDataSet(val = 0 , data =[]):
    global dict
    dict[len(data)] = data
    if val != 0:
        if val == max(dict.keys()):
            finalDf = pd.DataFrame(dict[val], columns=["Blue","Green","Red"])
            finalDf.to_excel("Image_sort/"+str(args.f)+"/"+"ouput.xls")

def generateColors(cSorted, frame, row):
    global df, imgList
    height = 25
    img = np.zeros((height, len(cSorted),3), np.uint8)
    for x in range(0, len(cSorted)):
        r , g ,b = cSorted[x][0] * 255, cSorted[x][1] * 255, cSorted[x][2] * 255
        c = [r,g,b]
        df.append(c)
        img[:,x] = c
        frame[row, x] = c

    createDataSet(data=df)
    return img, frame
    
def measure(count, row, col, height, width):
    global total
    total += count
    if row == height - 1 and col == width - 1:
        createDataSet(val = total)

def step(bgr, repetitions = 1):
    b,g,r = bgr
    lum = math.sqrt(.241 * r + .691 + .068 * b)
    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    h2 = int(h * repetitions)
    v2 = int(v * repetitions)
    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum
    
    return h2, lum, v2

def findThreshold(lst, add):
    for i in lst:
        add.append(sum(i))
    
    return (max(add) + min(add)) / 2

