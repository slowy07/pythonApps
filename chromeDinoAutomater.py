import pyautogui
from PIL import Image

# for mac and windows : from PIL import ImageGrab
import pyscreenshot as ImageGrab  # for linux user
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):

    for i in range(239, 452):
        for j in range(550, 650):
            if data[i, j] < 100:
                hit("up")
                return

    # for birds
    for i in range(310, 425):
        for j in range(390, 550):
            if data[i, j] < 100:
                hit("down")
                return

    return


if __name__ == "__main__":
    print("Dino game start in 5 second")
    time.sleep(4)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        isCollide(data)

        # draw cactus
        for i in range(315, 452):
            for j in range(550, 650):
                data[i, j] = 171

        image.show()
        break
