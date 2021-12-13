from __future__ import annotations

from itertools import permutations
from math import sqrt


def is_prime(n: int) -> bool:
    """
    >>> is_prime (67483)
    False
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False

    return True


def solution(n: int = 7) -> int:
    pandigital_str = "".join(str(i) for i in range(1, n + 1))
    perm_list = [int("".join(i)) for i in permutations(pandigital_str, n)]
    pandigitals = [num for num in perm_list if is_prime(num)]
    return max(pandigitals) if pandigitals else 0


if __name__ == "__main__":
    print(solution(7))
    print(is_prime(67483))
    print(is_prime(563))
    print(is_prime(87))
