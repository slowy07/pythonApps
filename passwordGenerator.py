import string as str
import secrets
import random

class passwordGenerator():

    @staticmethod

    def genSequence(conditions):
        possibleCharacters = [str.ascii_lowercase, str.ascii_uppercase, str.digits, str.punctuation]
        sequence = ""
        for x in range(len(conditions)):
            if conditions[x]:
                sequence += possibleCharacters[x]
            else:
                pass

        return sequence

    @staticmethod
    def generatePassword(sequence, passlength= 8):
        password = ''.join((secrets.choice(sequence) for i in range(passlength)))
        return password

class interface():
    hasCharacters = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True
    }
    @classmethod
    def changeHasCharacter(cls, change):
        try:
            cls.hasCharacters[change]
        except:
            print("invalid")
        else:
            cls.hasCharacters[change] = not cls.hasCharacters[change]
            print(f"{change} is now set to {cls.hasCharacters[change]}")
    @classmethod
    def showCharacters(cls):
        print(cls.hasCharacters)


    def generatingPassword(self, lenght):
        sequence = passwordGenerator.genSequence(list(self.hasCharacters.values()))
        print(passwordGenerator.generatePassword(sequence, lenght))

def listToVerticalString(list):
    toReturn = ""
    for member in list:
        toReturn += f"{member} \n"

    return toReturn

class running:

    def decideOperation():
        userInput = input("pass: ")
        try:
            int(userInput)
        except:
            interface.changeHasCharacter(userInput)
        else:
            interface().generatePassword(int(userInput))
        finally:
            print("\n\n")

    def run(self):
        menu = f"""Welcome to the PassGen App!
        Commands:
        <generate password ->
        <lenght of the password>
        commands to change the characters to be used to generate passwords:{listToVerticalString(interface.has_characters.keys())}"""
        
        print(menu)
    while True:
        decideOperation()


running().run()
