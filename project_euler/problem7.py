"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy

def set_num(number: int):
    """
    give return number of correct
    >>> set_num(20)
    73
    >>> set_num(100)
    547
    >>> set_num(10000)
    104743
    """
    f = numpy.array([True for _ in range(200000)])
    f[0:2] = False
    upper = int(numpy.sqrt(200000))

    for i in range(2, upper + 1):
        if f[i]:
            j = i * i
            counter = 0
            while j < 200000:
                f[j] = False
                j = (i * i) + (counter * i)
                counter += 1

    primes = numpy.where(f == True)[0]
    
    return primes[number]

if __name__ == "__main__":
    print(set_num(10000))
    print(set_num(100))