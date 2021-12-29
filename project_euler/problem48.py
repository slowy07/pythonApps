def solution() -> str:
    """
    >>> solution()
    '9110846700'
    """
    total = 0
    for i in range(1, 1001):
        total += i ** i
    return str(total)[-10:]


if __name__ == "__main__":
    import doctest

    print(solution())

    doctest.testmod(verbose=True)
