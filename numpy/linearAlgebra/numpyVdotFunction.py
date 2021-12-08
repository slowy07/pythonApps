import numpy as np

vector_a = 2 + 3j
vector_b = 4 + 5j

product = np.vdot(vector_a, vector_b)
print("Dot Product  : ", product)
