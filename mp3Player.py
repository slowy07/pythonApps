import os
from tkinter import *
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3

frameWindow = Tk()
frameWindow.minsize(300, 300)

# info song
listOfSong = []
realNames = []

v = StringVar()
songLabel = Label(frameWindow, textvariable=v, width=35)
index = 0


def directoryChooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realNames.append(audio["TIT2"].text[0])

            listOfSong.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSong[0])


directoryChooser()


def updateLabel():
    global index
    v.set(realNames[index])
    # return songName


def nextSong(event):
    global index
    index += 1
    pygame.mixer.music.load(listOfSong[index])
    pygame.mixer.music.play()
    updateLabel()


def prevSong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listOfSong[index])
    pygame.mixer.music.play()
    updateLabel()


def stopSong(event):
    pygame.mixer.music.stop()
    v.set("")
    # return songName


label = Label(frameWindow, text="music player")
label.pack()


listBox = Listbox(frameWindow)
listBox.pack()

realNames.reverse()

for items in realNames:
    listBox.insert(0, items)

realNames.reverse()
nextButton = Button(frameWindow, text="next Song")
nextButton.pack()

previousButton = Button(frameWindow, text="previous song")
previousButton.pack()

stopButton = Button(frameWindow, text="stop")
stopButton.pack()

nextButton.bind("<Button-1>", nextSong)
previousButton.bind("<Button-1>", prevSong)
stopButton.bind("<Button-1>", stopSong)

songLabel.pack()

frameWindow.mainloop()
