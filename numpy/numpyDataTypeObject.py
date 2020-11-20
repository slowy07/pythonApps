import numpy as np
 
# i4 represents integer of size 4 byte
# > represents big-endian byte ordering and
# < represents little-endian encoding.
dataType = np.dtype('>i4')
print("Byte order is:",dataType.byteorder)
print("Size is:", dataType.itemsize)
print("Data type is:",dataType.name)

#different between type and dtype.
#import numpy as np
#a = np.array([1])
#print("type is: ",type(a))
#print("dtype is: ",a.dtype)