"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


import functools


def get_lcm(*args):
    """
    The formula given on Wikipedia for computing the LCM is:
    lcm(a, b) = |a * b| / gcd(a, b)
    Where gcd(a, b) denotes the greatest common divisor of a and b

    When computing the LCM of more than two numbers it can be computed by
    iteratively computing the lcm of the current value and the next element of the list
    Example: lcm(a, b, c, d) = lcm(a, lcm(b, lcm(c, d)))

    >>> get_lcm(*range(1, 20))
    232792560
    """

    return functools.reduce(lcm, args)


def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


def gcd(num1, num2):
    if num1 == 0:
        return num2
    else:
        return gcd(num2 % num1, num1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
