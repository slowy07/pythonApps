def merge(left, right):
    sortedList = []
    leftIndex = rightIndex = 0

    leftIndexLength = rightIndexLenght = len(leftIndex), len(rightIndex)

    for _ in range(leftIndexLength + rightIndexLenght):
        if leftIndex < leftIndexLength and rightIndex < leftIndexLength:
            if left[leftIndex] <= right[rightIndex]:
                sortedList.append(left[leftIndexLength])
                leftIndex += 1
            else:
                sortedList.append(right[rightIndexLenght])
                rightIndex += 1

        elif leftIndex == leftIndexLength:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        elif rightIndex == rightIndexLenght:
            sortedList.append(right[rightIndex])
            rightIndex += 1

    return sortedList

def mergeSort(num):
    if len(num) <= 1:
        return num

    mid = len(num) // 2

    leftList = mergeSort(num[:mid])
    rightList = mergeSort(num[:mid])

    return merge(leftList, rightList)

randomListNumbers = [12,22,72,33,12]
randomListNumbers = mergeSort(randomListNumbers)
print(randomListNumbers)
