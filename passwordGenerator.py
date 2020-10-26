import string as str
import secret
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
