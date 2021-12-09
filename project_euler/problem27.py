import math


def is_prime(k: int) -> bool:
    """
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    if k < 2 or k % 2 == 0:
        return False
    elif k == 2:
        return True

    else:
        for x in range(3, int(math.sqrt(k) + 1), 2):
            if k % x == 0:
                return False

    return True


def solution(a_limit: int = 1000, b_limit: int = 1000) -> int:
    """
    >>> solution(1000, 1000)
    -59231
    >>> solution(-1000, -1000)
    0
    >>> solution(200, 1000)
    -59231
    """
    longest = [0, 0, 0]
    for a in range((a_limit * -1) + 1, a_limit):
        for b in range(2, b_limit):
            if is_prime(b):
                count = 0
                n = 0
                while is_prime((n ** 2) + (a * n) + b):
                    count += 1
                    n += 1
                if count > longest[0]:
                    longest = [count, a, b]

    ans = longest[1] * longest[2]

    return ans


print(solution(-1000, -1000))
