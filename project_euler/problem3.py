"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy


def prime_factorization(number):
    number_bound = int(numpy.sqrt(number)) + 1

    for i in range(2, number_bound):
        if number % i == 0:
            return i

    return number


def set_answer(set_number):
    """
    get result answer
    >>> set_answer(600851475143)
    6857
    >>> set_answer(3000)
    5
    """
    while True:
        prime_fac = prime_factorization(set_number)
        if prime_fac < set_number:
            set_number //= prime_fac
        else:
            return set_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
