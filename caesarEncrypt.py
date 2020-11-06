def encrypt(text, lenght):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) + lenght - 65) % 26 + 65)
        else:
            result += chr((ord(char) + lenght - 97) % 26 + 97)
        
        
    return result

text = "zulkrepetes make cpplest and templest ostest"
lenght = 4
print("message :", text)
print("shift pettern :" + str(lenght))
print("key :", encrypt(text,lenght))