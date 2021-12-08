# left_shift() function

import numpy as np

in_num = 5
bit_shift = 2

print("Input  number : ", in_num)
print("Number of bit shift : ", bit_shift)

out_num = np.left_shift(in_num, bit_shift)
print("After left shifting 2 bit  : ", out_num)
