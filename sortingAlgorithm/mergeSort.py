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
