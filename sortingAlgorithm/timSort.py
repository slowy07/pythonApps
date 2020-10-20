RUN = 32
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + 1])
    for i in range(0, len2):
        right.append(arr[m + 1 +i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        l += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timSort(arr, num):
    for i in range(0, num, RUN):
        insertionSort(arr, i, min((i + 31), (num - 1)))
    size = RUN
    while size < num:
        for left in range(0, num, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (num - 1))
            merge(arr, left, mid, right)
        size = 2 * size

def printArray(arr, num):
    for i in range(0, num):
        print(arr[i], end=" ")

if __name__ == "__main__":
    getSize = int(input("enter element size of arr:"))
    print("enter element of arr")
    '''
        ouput:
        enter element size of arr: 3
        given arr is
        3 2 1
        after sorting
        1 2 3
    '''
    arr = list(map(int, input().split()))
    print("given arr is")
    printArray(arr, getSize)
    timSort(arr, getSize)
    print("after sorting")
    printArray(arr, getSize)
