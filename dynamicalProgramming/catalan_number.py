def catalan_number(upper_limit: int) -> "list[int]":
    if upper_limit < 0:
        raise ValueError("limit for the catalan number must > 0")

    catalan_list = [0] * (upper_limit + 1)
    catalan_list[0] = 1

    if upper_limit > 0:
        catalan_list[1] = 1

    for i in range(1, upper_limit + 1):
        for j in range(i):
            catalan_list[i] += catalan_list[j] * catalan_list[i - j - 1]

    return catalan_list


if __name__ == "__main__":
    print("catalan list")
    print("enter -1 at any time to quit")
    print("\n Enter the upper limit ( > 0 ) for the catalan number sequence", end="")

    try:
        while True:
            N = int(input().strip())
            if N < 0:
                print("quiting")
                break
            else:
                print(f"the catalan number from 0 through {N} are :")
                print(catalan_number(N))
                print("try the another limit for the sequence", end="")
    except (NameError, ValueError):
        print("invalid input")

    import doctest

    doctest.testmod()
