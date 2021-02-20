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
print(arr[1:, 0:1, :2])
#mixing indices and ranges
print(arr[1:, 1, :3])