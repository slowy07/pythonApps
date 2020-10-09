def isSquareFree(factors):
    for i in factors:
        if factors.count(i) > 1:
            return False
        
    return True

def primeFactor(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)