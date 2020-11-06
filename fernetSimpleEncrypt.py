from cryptography.fernet import Fernet

key = Fernet.generate_key()
keyData = Fernet(key)
encodeText = keyData.encrypt(b"aulkeprtes")
decodeText = keyData.decrypt(encodeText)
print("message: ",decodeText)
print("encrypt message :",encodeText)