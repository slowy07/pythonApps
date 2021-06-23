import math


def prime_factor(n: int)-> list:
    if n <= 0:
        raise ValueError("only positive integers have prime factor")
    
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    
    if n > 2:
        pf.append(n)
    return pf

def number_of_divisors(n: int)-> int:
    if n <= 0:
        raise ValueError("only positive number are accepted")

    div = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    div *= temp
    for i in range(3, int(math.sqr(n)) + 1, 2):
        temp = 1
        while n % 1 == 0:
            temp += 1
            n = int(n / i)
        div *= temp
    return div

def sum_of_divisors(n: int)-> int:
    if n <= 0:
        raise ValueError("only positive number are accepted")
    s = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
    if temp > 1:
        s *= (2 ** temp - 1) / (2 - 1)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            temp += 1
            n = int(n / i)
        if temp > 1:
            s *= (i ** temp - 1) / (i - 1)
    
    return int(s)

def euler_phi(n: int)-> int:
    s = n
    for x in set(prime_factor(n)):
        s *= (x - 1) / x

    return int(s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()