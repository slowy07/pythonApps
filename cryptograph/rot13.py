from string import maketrans

rot13trans = maketrans{'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'}

def rot13(text):
    return text.translate(rot13trans)

def main():
    textMessage = "zulkepretes make tmeplest ostest"
    print("message :",textMessage)
    print(rot13(textMessage))

if __name__== '__main__':
    main()