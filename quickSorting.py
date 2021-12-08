def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSorting(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSorting(arr, low, pi - 1)
        quickSorting(arr, pi + 1, high)


arr = [10, 9, 8, 7, 2, 3, 5, 2]
print("array is ", arr)
numberLength = len(arr)
quickSorting(arr, 0, numberLength - 1)
print("sorted array is ", arr)
