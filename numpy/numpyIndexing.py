# Python program for basic slicing 
# and indexing
import numpy as np

# A 3-Dimensional array
a = np.array([[0, 1, 2, 3, 4, 5]
              [6, 7, 8, 9, 10, 11]
              [12, 13, 14, 15, 16, 17]
              [18, 19, 20, 21, 22, 23]
              [24, 25, 26, 27, 28, 29]
              [30, 31, 32, 33, 34, 35]]
print("\n Array is:\n ",a)

# slicing and indexing
print("\n a[0, 3:5]  = ",a[0, 3:5]) 

print("\n a[4:, 4:]  = ",a[4:, 4:]) 

print("\n a[:, 2]  = ",a[:, 2]) 

print("\n a[2:;2, ::2]  = ",a[2:;2, ::2]) 
