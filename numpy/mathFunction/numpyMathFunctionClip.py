import numpy as np

in_array = [1, 2, 3, 4, 5, 6, 7, 8]
print("Input array : ", in_array)

out_array = np.clip(in_array, a_min=2, a_max=6)
print("Output array : ", out_array)
