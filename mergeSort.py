
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
            oriList[base] = R[0]
            R.remove(R[0])

        base += 1

    while len(L) > 0:
        oriList[base] = L[0]
        L.remove(L[0])
        base += 1
    while len(R) > 0:
        oriList[base] = R[0]
        R.remove(R[0])
        base += 1


def mergeSort(L, left, right):
    if left + 1 >= right:
        return
    mid = left + (right - left) // 2
    mergeSort(L, left, mid)
    mergeSort(L, mid, right)
    merge(L, left, mid, right)

print("unsorted data ->", lst)
mergeSort(lst, 0, number)
print("get sorted ->", lst)