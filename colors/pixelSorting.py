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



