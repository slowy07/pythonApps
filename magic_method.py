"""class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("deleted")

person = People("james", 25)
"""


class Square:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __add__(self, other):
        return Square(self.side1 + other.side1, self.side2 + other.side2)

    def __repr__(self):
        return (
            f"side 1: {self.side1} side2: {self.side2} result {self.side1 + self.side2}"
        )


square1 = Square(50, 20)
square2 = Square(50, 30)
result = square1 + square2
print(result)
