# unpackbits() function
import numpy as np

# creating an array using
# array function
a = np.array([[2], [7], [23]], dtype=np.uint8)

# packing elements of an array
# using packbits() function
b = np.unpackbits(a, axis=1)

print(b)
