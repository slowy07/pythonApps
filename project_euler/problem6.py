"""
https://projecteuler.net/problem=6
"""

import numpy


def summary_square(start, end):
    return sum(i ** 2 for i in range(start, end))


def square_sum(start, end):
    return numpy.sum(numpy.arange(start, end)) ** 2


def generate_diff(start, end):
    """
    total result
    >>> generate_diff(1, 101)
    25164150
    >>> generate_diff(1, 100)
    24174150
    """
    a = summary_square(start, end)
    b = square_sum(start, end)

    return numpy.abs(a - b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
