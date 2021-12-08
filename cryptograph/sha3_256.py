import sys
import hashlib

if sys.version_info < (3, 6):
    import sha3

# initialize a string
str = "zulkepretes"
# encode the string
encoded_str = str.encode()
# create sha3-256 hash objects
obj_sha3_256 = hashlib.sha3_256(encoded_str)
# print in hexadecimal
print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())
