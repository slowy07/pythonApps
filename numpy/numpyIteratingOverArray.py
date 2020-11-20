import numpy as np
a = np.arange(12)
 
# shape array with 3 rows and 
# 4 columns
a = a.reshape(3,4)
 
print('Original array is:')
print(a)
print()
 
print('Modified array is:')
 
# iterating  an array
for x in np.nditer(a):
    print(x)