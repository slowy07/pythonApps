import numpy as np


a = np.array([9, 3, 1, 7, 4, 3, 6])
print('Original array:\n', a)
b = np.argsort(a)
print('Sorted indices of original array->', b)

c = np.zeros(len(b), dtype = int)
for i in range(0, len(b)):
    c[i]= a[b[i]]
print('Sorted array->', c)