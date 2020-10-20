# pip install PyQRCode

import pyqrcode
import PIL
from pyqrcode import QRCode

generateData = input("enter text to convert :")
imageName = input("enter image name to save :")
imageNameResult = imageName + ".png"
url = pyqrcode.create(generateData)

url.png(imageNameResult, scale = 6)
