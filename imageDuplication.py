import os
import sys
from PIL import Image

def duplicateMe(file, i):
    picture = Image.open(file)
    dim = os.stat(file).st_size

    picture.save(str(i+1)+".jpg", "JPEG", optimize=True, quality=100)

def utama():
    verbose=False
    if(len(sys.argv)>1):
        if(sys.argv[1].lower()=="-v"):
            verbose=True
    pwd=os.getcwd()
    for i in range(10):
        file = "<filename>"
        duplicateMe(file, i)

if __name__ == '__main__':
    utama()
