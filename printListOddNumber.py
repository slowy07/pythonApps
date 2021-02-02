number = list(map(int, input().split()))
oddList = [i for i in number if i % 2 !=0]
print(oddList)
#exit()

number = int(input("Enter the limit: "))
if number <= 0:
    print("invalid")
else:
    oddList = [i for i in range(1, number + 1, 2)]
    print(oddList)

number = map(list(int, input().split()))
even = []
odd = []
for i in range(number):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)