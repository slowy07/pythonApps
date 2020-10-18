#simple quick sort

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quickSort(nums):
    def _quickSort(items, low, high):
        if low < high:
            splitIndex = partition(items, low, high)
            _quickSort(items, low, splitIndex)
            _quickSort(items, splitIndex + 1, high)

    _quickSort(nums, 0, len(nums) - 1)

randomListNums = [12,54,12,99,52]
quickSort(randomListNums)
print(randomListNums)
