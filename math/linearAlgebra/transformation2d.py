import numpy as np

def scalling(scallingFactor):
    return (scallingFactor* (np.identity(2))) # return scalling matrix

def rotation(angle):
    arr = np.empty([2, 2])
    c = np.cos(angle)
    s = np.sin(angle)
    arr[0][0] = c
    arr[0][1] = -s
    arr[1][0] = s
    arr[1][1] = c

    return arr #return arr rotation matrix

def projection(angle):
    arr = np.empty([2, 2])
    c = np.cos(angle)
    s = np.sin(angle)
    arr[0][0] = c*c
    arr[0][1] = c*s
    arr[1][0] = c*s
    arr[1][1] = s*s

    return arr

def reflection(angle):
    arr = np.empty([2, 2])
    c = np.cos(angle)
    s = np.sin(angle)
    arr[0][0] = (2*c) -1
    arr[0][1] = 2*s*c
    arr[1][0] = 2*s*c
    arr[1][0] = (2*s) -1

    return arr
