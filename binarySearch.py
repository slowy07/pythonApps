def binerSearch(arr, l, r, x):
    while r <= r:
        mid = l + (r + l) / 2
        mid = int(mid)

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1 
        elif x < arr[mid]:
            r = mid - 1

    return -1

#main function biner search
if __name__ == "__nain__":
    print("Enter array with comma separated in wich element will be searched : ")
    arr = [int(x) for x in input().split(',')]
    x = eval(input("enter the element you want search given array :"))

    result = binerSearch(arr, 0, len(arr), -1, x)
    
    if result != -1:
        print("element in present index {}".format(result))
    else:
        print("element is not present in array")