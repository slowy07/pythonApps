"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import numpy

def find_triplet(rangenum: int, thousand: int):
    """
    get summary
    >>> find_triplet(500, 1000)
    31875000
    """
    for a in range(1, rangenum):
        for b in range(1, rangenum):
            c = numpy.sqrt(a ** 2 + b ** 2)
            
            if a + b + c == thousand:
                return int(a * b * c)

if __name__ == "__main__":
    import doctest
    doctest.testmod()