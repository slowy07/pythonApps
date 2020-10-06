number = int(input("give the number of the element : "))
print("enter number separated by spaces ")
tlist = list(map(int, input().split()))
k = max(tlist)
number = len(tlist)

def countingSort(tlist, k, number):
    """
    create counting sort
    """
    countList = [0] * (k+1)
    
    for i in range(0, number):
        countList[tlist[i]] += 1

    for i in range(1, k+1):
        countList[i] = countList[i] + countList[i - 1]

    flist = [0] * (number)
    for i in range(number - 1, -1, -1):
        countList[tlist[i]] = countList[tlist[i]] - 1
        flist[countList[tlist[1]]] = (tlist[i])

        return True
    
    flist = countingSort(tlist, k, number)
    print(flist)