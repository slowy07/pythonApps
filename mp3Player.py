import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *


frameWindow = Tk()
frameWindow.minsize(300,300)

#info song
listOfSong = []
realNames = []

v = StringVar()
songLabel = Label(frameWindow, textVariable=v, width=35)
index = 0

def directoryChooser():
    directory = askdirectory()
    os.chdir(directory)

    