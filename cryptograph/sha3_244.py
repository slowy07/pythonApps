import hashlib
import sys

if sys.version_info < (3, 6):
    import sha3

# initiating the "s" object to use the
# sha3_224 algorithm from the hashlib module.
s = hashlib.sha3_224()
# will output the name of the hashing algorithm currently in use.
print(s.name)
# will output the Digest-Size of the hashing algorithm being used.
print(s.digest_size)
# providing the input to the hashing algorithm.
s.update(b"zulkepretes")
print(s.hexdigest())
