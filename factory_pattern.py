from abc import ABCMeta, abstractstaticmethod

class LPerson(metaclass = ABCMeta):    
    @abstractstaticmethod
    def personMethod():
        """iface method"""

class Student(LPerson):
    def __init__(self):
        self.name = "zulkepretes"

    def personMethod(self):
        print("Student name {}".format(self.name))

class Teacher(LPerson):
    def __init__(self):
        self.name = "sayutes"
    
    def personMethod(self):
        print("Teacher name {}".format(self.name))

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("invalid type")
        
        return -1

if __name__ == '__main__':
    choice = input("what category (Student / Teacher): ")
    person = PersonFactory.build_person(choice)
    person.personMethod()