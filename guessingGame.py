import random
import time

print("welcome to guessing game")
time.sleep(1)

name = input("whats your name :")
time.sleep(1)
print(f"okay {name} let's go!")
a = comGuess = random.randint(0,100)
count = 0

while True: #looping
    userGuess = int(input("enter number u guess (0 - 100) :"))
    if userGuess < comGuess:
        print("to high")
        comGuess = random.randint(a, 100)
        a += 1
        count = 1

    elif userGuess > comGuess:
        print("lower")
        comGuess = random.randint(0, a)
        a += 1
        count = 1
    
    elif userGuess == comGuess and count == 0:
        print("you right, magician !")

    else:
        print("congratulation you're correctly")