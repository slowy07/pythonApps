from math import sqrt


def sum_of_divisor(n: int) -> int:
    total = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0 and i != sqrt(n):
            total += i + n // i
        elif i == sqrt(n):
            total += i

    return total - n


def solution(n: int = 10000) -> int:
    """
    >>> solution(10000)
    31626
    """
    total = sum(
        i
        for i in range(1, n)
        if sum_of_divisor(sum_of_divisor(i)) == i and sum_of_divisor(i) != i
    )
    return total


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
