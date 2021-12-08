# packbits() function
import numpy as np

# creating an array using
# array function
a = np.array([[[1, 0, 1], [0, 1, 0]], [[1, 1, 0], [0, 0, 1]]])

# packing elements of an array
# using packbits() function
b = np.packbits(a, axis=-1)

print(b)
