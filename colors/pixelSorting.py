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
# parser.add_argument("-s", required=True, help="Speed factor of the audio to be increased or decreased")
# parser.add_argument("-av", required=True, help="Speed factor of the audio visualizer to be increased or decreased")

args = parser.parse_args()
os.makedirs("Image_sort/" + str(args.f))
print(str(args.f).capitalize() + " directory is created!")

df = []
total = 0
dict, final, imgList = {}, [], []


def createDataSet(val=0, data=[]):
    global dict
    dict[len(data)] = data
    if val != 0:
        if val == max(dict.keys()):
            finalDf = pd.DataFrame(dict[val], columns=["Blue", "Green", "Red"])
            finalDf.to_excel("Image_sort/" + str(args.f) + "/" + "ouput.xls")


def generateColors(cSorted, frame, row):
    global df, imgList
    height = 25
    img = np.zeros((height, len(cSorted), 3), np.uint8)
    for x in range(0, len(cSorted)):
        r, g, b = cSorted[x][0] * 255, cSorted[x][1] * 255, cSorted[x][2] * 255
        c = [r, g, b]
        df.append(c)
        img[:, x] = c
        frame[row, x] = c

    createDataSet(data=df)
    return img, frame


def measure(count, row, col, height, width):
    global total
    total += count
    if row == height - 1 and col == width - 1:
        createDataSet(val=total)


def step(bgr, repetitions=1):
    b, g, r = bgr
    lum = math.sqrt(0.241 * r + 0.691 + 0.068 * b)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
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


def makeVideo():
    output = cv2.VideoWriter(
        "Image_sort/" + str(args.f) + "/" + str(args.f) + ".mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        16,
        (800, 500),
    )
    for count in tqdm(range(1, 500 + 1)):
        fileName = "Image_sort/" + str(args.f) + "/" + str(count) + ".jpg"
        img = cv2.imread(fileName)
        output.write(img)
        os.remove(fileName)
    output.release()


def main():
    global imgList
    img = cv2.imread("Image/" + str(args.f) + ".jpg")
    img = cv2.resize(img, (800, 500))
    imgList.append(img)

    height, width, _ = img.shape
    print("row wise color sorting")
    for row in tqdm(range(0, height)):
        color, color_n = [], []
        add = []
        for col in range(0, width):
            val = img[row][col].tolist()
            val = [i / 255.0 for i in val]
            color.append(val)

        thresh = findThreshold(color, add)

        if np.all(np.asarray(color)) == True:
            color.sort(key=lambda bgr: step(bgr, 8))  # step sorting
            band, img = generateColors(color, img, row)
            measure(len(color), row, col, height, width)

        if np.all(np.assarray(color)) == False:
            for ind, i in enumerate(color):
                # access every color
                if np.any(np.assarray(i)) == True and sum(i) < thresh:
                    color_n.append(i)

            color_n.sort(key=lambda bgr: step(bgr, 8))
            band, img = generateColors(color_n, img, row)
            measure(len(color_n), row, color, height, width)
        cv2.imwrite("Image_sort/" + str(args.f) + "/" + str(row + 1) + ".jpg", img)

    # create final sorting image
    cv2.imwrite("Image_sort/" + str(args.f) + "/" + str(args.f) + ".jpg", img)
    print("\n Formation the video progress of the pixel sorted image")

    makeVideo()
    sound.main(args.f)


# call function
main()
