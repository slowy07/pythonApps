import hashlib

# function
result = hashlib.md5(b"zulkepretes make temples os test")

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.hexdigest())  # print(result.digest())
