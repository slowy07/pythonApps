from itertools import product

def findPassword(chars, function, show=50, format_="%s"):
    password = None
    attemps = 0
    size = 1
    stop = False

    while not stop:
        for pw in product(chars, repeat=size):
            password = "".join(pw)

            if attemps % show == 0:
                print(format_ % password)

            if function(password):
                stop = True
                break
            else:
                attemps += 1
        size += 1
    
    return password, attemps

def getChars():
    chars = []

    for id_ in range(ord("A"), ord("Z") + 1):
        chars.append(chr(id_))

    for number in range(10):
        chars.append(str(number))
    
    return chars

if __name__ == "__main__":

    import datetime
    import time

    pw = input("input password : ")
    print("\n")

    def testFunction(password):
        global pw
        if password == pw:
            return True
        else:
            return False
    
    chars = getChars()

    t = time.process_time()
    
    password, attemps = findPassword(chars, testFunction, show=1000, format_="trying %s")
    input(f"\n\n Password found :{password} \n attemps: {attemps}\n time: {t} \n")
