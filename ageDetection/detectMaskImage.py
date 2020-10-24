from tensorflow.keras.application.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
import os

def maskImage():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    ap.add_argument("-f", "--face", typ=str, default="face-detector", help="path to detector model directory")
    ap.add_argument("-m", "--model", type=str, default="maskDetector.model", help="path to trained face mask detector model")
    ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detection")
    args = vars(ap.parse_args())


    print("[INFO] loading face detector model..")
    model = load_model(args['model'])

    #load the input image from disk
    image = cv2.imread(args["image"])
    orig = image.copy()
