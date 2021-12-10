def solution(pence: int = 200) -> int:
    """
    >>> solution(200)
    73681
    """
    coins = [1,2,5,10,20,50,100,200]
    number_of_ways = [0] * (pence + 1)
    number_of_ways[0] = 1

    for coin in coins:
        for i in range(coin, pence + 1, 1):
            number_of_ways[i] += number_of_ways[i - coin]

    return number_of_ways[pence]

print(solution(200))
