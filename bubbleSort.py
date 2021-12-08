def bubbleSort(arr):
    number = len(arr)

    for i in range(number):
        notSwap = True
        for j in range(0, number - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    notSwap = False

        if notSwap:
            break


arr = [64, 22, 32, 21, 82, 11]

bubbleSort(arr)
print("sorted array ")
for i in range(len(arr)):
    print("%d" % arr[i])
