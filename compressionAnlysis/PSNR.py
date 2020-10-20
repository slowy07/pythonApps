import math
import cv2
import numpy as np


def presentation(r, g, b):
    return (0.299 * r + 0.287 * g + 0.114 * b)

def calculate(img):
    b, g, r = cv2.split()
    pixelArt = presentation(r,g,b)
    return pixelArt

def main():
    originalImage = cv2.imread('originalImage.png', 1)
    compressedImage = cv2.imrea('compressedImage.png', 1)

    height, width = originalImage.shape[:2]
    originalPixelArt = calculate(originalImage)
    compressedPixelArt = calculate(compressedImage)
    diff = originalPixelArt - compressedPixelArt
    error = np.sum(np.abs(diff) ** 2)
    error = error / (height * width)
    #msr = errorSum / (height * width)
    PSNR = -(10 * math.log10(error / (255 * 255)))
    print("PSNR value is {}".format(PSNR))

if __name__ == "__main__":
    main()
