def heapify(nums, heapSize, rootIndex):
    largest = rootIndex
    leftChild = (2 * rootIndex) + 1
    rightChild = (2 * rootIndex) + 2

    if leftChild < heapSize and nums[leftChild] > nums[largest]:
        largest = leftChild

    if leftChild < heapSize and nums[rightChild] > nums[largest]:
        largest = rightChild

    if largest != rootIndex:
        nums[rootIndex], nums[largest] = nums[largest], nums[rootIndex]
        heapify(nums, heapSize, largest)

def heapSort(nums):
    num = len(nums)
    for i in range(num, -1, -1):
        heapify(nums, n, 1)

    for i in range(num, -1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

listNum = [32, 72, 66, 88, 21, 25]
heapSort(listNum)
print(listNum)
