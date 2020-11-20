from string import maketrans

rot13trans = maketrans{'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'}

def rot13(text):
    return text.translate(rot13trans)

def main():
    textMessage = "besok saya pergi ke amerika"
    print("message :",textMessage)
    print(rot13(textMessage))

if __name__== '__main__':
    main()