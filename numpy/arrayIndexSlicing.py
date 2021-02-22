import numpy as np

arr = np.array([
    [[11, 12, 13, 14],
     [13, 14, 15, 19]],

    [[15, 16, 17, 21],
     [63, 92, 36, 18]],
    
    [[98, 31, 81, 23],
     [17, 18, 19.5, 43]]
])

"""print(arr.shape)
print(arr)"""
print(arr[1])
print(arr[1,1])
#single element
print(arr[1, 1, 2])


#sub array using ranges
print("\nsub array using ranges\n",arr[1:, 0:1, :2])
#mixing indices and ranges
print("\nmixing indices and ranges\n",arr[1:, 1, :3])

#using fewer indices
print("\nusing fewer indices \n",arr[1])


"""
[[15. 16. 17. 21.]
 [63. 92. 36. 18.]]
[63. 92. 36. 18.]
36.0

sub array using ranges
 [[[15. 16.]]

 [[98. 31.]]]

mixing indices and ranges
 [[63.  92.  36. ]
 [17.  18.  19.5]]

using fewer indices 
 [[15. 16. 17. 21.]
 [63. 92. 36. 18.]]
 """