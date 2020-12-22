import numpy as np
 
# Creating an array using array
# function
a = np.array([[1, 2], [3, 4]])
 
# Creating an array using array
# function
b = np.array([8, 18])
 
print(("Solution of linear equations:", np.linalg.solve(a, b)))