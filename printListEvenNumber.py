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

"""
>>> 20
>>> enter the require range : 90
>>> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90]
"""