from numpy import linalg as line
 
# Creating an array using diag 
# function
a = np.diag((1, 2, 3))
 
print("Array is :",a)
# using eig() function
c, d = line.eig(a)
 
print("Eigen value is :",c)
print("Eigen value is :",d)