from __future__ import annotations

sieve = [True] * 100001
i = 2

while i * i <= 100001:
    if sieve[i]:
        for j in range(i * i, 100001, i):
            sieve[j] = False
    i += 1


def is_prime(n: int) -> bool:
    """
    >>> is_prime(23)
    True
    """
    return sieve[n]


odd_composites = [num for num in range(3, len(sieve), 2) if not is_prime(num)]


def compute_nums(n: int) -> list[int]:
    """
    >>> compute_nums(2)
    [5777, 5993]
    """
    if not isinstance(n, int):
        raise ValueError("n must integer")
    if n <= 0:
        raise ValueError("n must >= 0")

    list_nums = []

    for num in range(len(odd_composites)):
        i = 0
        while 2 * i * i <= odd_composites[num]:
            rem = odd_composites[num] - 2 * i * i
            if is_prime(rem):
                break

            i += 1
        else:
            list_nums.append(odd_composites[num])
            if len(list_nums) == n:
                return list_nums

    return []


def solution() -> int:
    return compute_nums(1)[0]


if __name__ == "__main__":
    import doctest

    print("solution: {}".format(solution()))
    doctest.testmod(verbose=True)
