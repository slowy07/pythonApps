"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(n):
    """
    return number
    >>> sum_multiples(10)
    23
    >>> sum_multiples(100)
    2318
    >>> sum_multiples(1000)
    233168
    """

    multiple = [num for num in range(n) if num % 3 == 0 or num % 5 == 0]
    return sum(multiple)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
