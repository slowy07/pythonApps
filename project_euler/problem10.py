"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from doctest import DONT_ACCEPT_TRUE_FOR_1
import numpy


def set_num(problem_num: int):
    """
    finding algorithm prime
    >>> set_num(2000000)
    142913828922
    """
    number = 5000000
    f = numpy.array([True for _ in range(number)])
    f[0:2] = False
    upper = int(numpy.sqrt(number))

    for i in range(2, upper + 1):
        if f[i]:
            j = i * i
            counter = 0
            while j < number:
                f[j] = False
                j = (i * i) + (counter * i)
                counter += 1

    primes = numpy.where(f == True)[0]
    indx = numpy.where(primes < problem_num)[0]
    subset = primes[indx]

    return sum(subset)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
