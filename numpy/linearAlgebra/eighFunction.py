from numpy import linalg as line

# Creating an array using array
# function
a = np.array([[1, -2j], [2j, 5]])

print("Array is :", a)
# using eigh() function
c, d = line.eigh(a)

print("Eigen value is :", c)
print("Eigen value is :", d)
