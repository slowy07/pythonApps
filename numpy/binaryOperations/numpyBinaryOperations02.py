import numpy as np
 
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
  
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
   
out_arr = np.bitwise_and(in_arr1, in_arr2) 
print ("Output array after bitwise_and: ", out_arr) 
