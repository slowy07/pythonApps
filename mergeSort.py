
lst = []
number = int(input("Enter number of element in list: "))

for i in range(number):
    temp = int(input("Enter element "+str(i + 1) + ': '))
    lst.append()

def merge(oriList, left, mid, right):
    L, R = [], []
    for i in range(left, mid):
        L.append(oriList[i])
    for i in range(mid, right):
        R.append(oriList[i])
    
    base = left

    while len(L) > 0 and len(R) > 0:
        if L[0] < R[0]:
            oriList[base] = L[0]
            L.remove(L[0])
        else:
            if l