from __future__ import annotations


def is_palindrome(n: int | str) -> bool:
    """
    >>> is_palindrome(909)
    True
    """
    n = str(n)
    return True if n == n[::-1] else False


def solution(n: int = 1000000) -> int:
    total = 0
    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]):
            total += i
    return total


if __name__ == "__main__":
    print(solution(1000000))
