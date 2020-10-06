number = int(input("give the number of the element : "))
print("enter number separated by spaces ")
tlist = list(map(int, input().split()))
k = max(tlist)
number = len(tlist)

def countingSort():
    """
    create counting sort
    """
    