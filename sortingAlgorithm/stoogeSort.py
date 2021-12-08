def stoogeSort(arr, l, h):
    if l >= h:
        return 0

    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)

        stoogeSort(arr, l, (h - t))
        stoogeSort(arr, l + t, (h))
        stoogeSort(arr, l, (h - t))


arr = [1, 6, 4, 5, 7, 12]
n = len(arr)
stoogeSort(arr, 0, n - 1)
print(arr)
