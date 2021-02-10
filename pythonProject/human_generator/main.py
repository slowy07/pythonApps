import men
import female
from prettytable import PrettyTable


table = PrettyTable()

def set_human(sex):
    if sex == 'M' or sex == 'MALE' or sex == 'Male' or sex == 'male' or sex == 'm':
        table.field_names = ["Created date", "Human id", "Name ","Surename","Hairstyle", "Country"]
        table.add_rows(
            [
                [men.get_datetime(), men.human_id, name, surename, men.get_hair_men(), men.get_country()]
            ]
        )
        print(table.get_string())
    elif sex == 'F' or sex == 'Female' or sex == 'Female' or sex == 'female' or sex == 'f':
        table.field_names = ["Created date", "Human id", "Name ","Surename","Hairstyle", "Country"]
        table.add_rows(
            [
                [female.get_datetime(), female.human_id, name, surename, female.get_hair_men(), female.get_country()]
            ]
        )
        print(table.get_string())
    else:
        print("error input")
        pass


name = str(input("name :"))
surename = str(input("surename :"))
sex = str(input("Male (M) or Female (F): "))
contain = False
for chardata in surename:
    if chardata.isdigit():
        contain = True
        pass
if contain == True:
    print("your name have number ?")
else:
    set_human(sex)