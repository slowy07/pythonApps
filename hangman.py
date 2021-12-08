import time
import random

name = input("Whats ur name :")

print("hello " + name + "!\ntime to play hangman")
time.sleep(1)

print("time to guess, \n Hint:its Fruit!")
time.sleep(0.5)

keyWord = """apple banana mango strawberry 
orange rambutan pineapple lemon coconut watermelon 
melon cherry papaya berry peach lychee muskmelon
pear starfruit
"""

keyWord = keyWord.split(" ")
word = random.choice(keyWord)

guesses = ""
turns = 5

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")

            failed += 1

    if failed == 0:
        print("you won!")
        break

    guess = input("guess a character :")

    if not guess.isalpha():
        print("enter only letter")
        continue
    elif len(guess) > 1:
        print("only single letter")
        continue
    elif guess in guesses:
        print("you're already guessed that letter")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong !")

        print("you have ", +turns, "more guesses \n")
        if turns == 0:
            print("you lose")
