# around() function

import numpy as np

in_array = [0.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print("Input array : \n", in_array)

round_off_values = np.around(in_array)
print("\nRounded values : \n", round_off_values)


in_array = [0.53, 1.54, 0.71]
print("\nInput array : \n", in_array)

round_off_values = np.around(in_array)
print("\nRounded values : \n", round_off_values)

in_array = [0.5538, 1.33354, 0.71445]
print("\nInput array : \n", in_array)

round_off_values = np.around(in_array, decimals=3)
print("\nRounded values : \n", round_off_values)
