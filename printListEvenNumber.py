
from builtins import list

listNumber = list(map(int, input().split()))
evenList = [i for i in listNumber if i%2 == 0]
print(evenList)
#exit()

number = int(input("enter the require range :"))
list = []


if number < 0:
    print("not valid number, enter the positive number ")
else:
    for i in range(0, number + 1):
        if i % 2 == 0:
            list.append(i)

print(list)