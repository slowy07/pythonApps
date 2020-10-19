from os import chdir
from os import makedirs
from os import rename
from os import removedirs
from os.path import exitsts
from os.path import pardir
from shutil import copytree
from shutil import move

def createDirectory(name):
    if exitsts(pardir + "\\" + name):
        print("folder already exitsts")
    else:
        makedirs(pardir + "\\" + name)

def deleteDirectory(name):
    removedirs(name)

def renameDirectory(direct, name):
    rename(direct, name)

def setWorkingDirectory():
    chdir(pardir)

def backupFile(nameDir, folder):
    copytree(pardir, nameDir + ':\\' + folder)

def moveFolder(fileName, nameDir, folder):
    if not exitsts(nameDir + ':\\' + folder):
        makedirs(nameDir + ':\\' + folder)
    move(fileName, nameDir + ':\\' + folder + '\\')
