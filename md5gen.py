import hashlib #pip install hashlib


stringHash = input("enter message to generate code :")
resultHash = hashlib.md5(stringHash.encode())
print("the hexadecimal equivalent is :", end="")
print(resultHash.hexdigest())
