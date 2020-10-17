#windows only


from __future__ import print_function
import os
from _winreg import *


def sidToUser(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]

        return user

    except:
        return  sid

def returnDir():
    dirs = ['c:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$RECYCLE.BIN\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirlist:
        files = os.listdir(recycleDir + sid)
        user = sidToUser(sid)

        print("\n [x] Listing files :"+str(user))
        for file in files:
            print("[x] found :"+st(file))

def main():
    recycleDir = returnDir()
    findRecycled(recycleDir)


if __name__ == "__main__":
    main()
