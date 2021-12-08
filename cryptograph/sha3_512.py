import sys
import hashlib

if sys.version_info < (3, 6):
    import sha3
str = "zulkepretes"
# create a sha3 hash object
hash_sha3_512 = hashlib.new("sha3_512", str.encode())
print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest())
