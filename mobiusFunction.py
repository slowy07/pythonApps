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
    if number > 1:
        factors.append(number)

    return factors


def mobiusFunction(number):
    """
    define mobius fnction
    """
    factors = primeFactor(number)
    if isSquareFree(factors):
        if len(factors) % 2 == 0:
            return 1
        elif len(factors) % 2 != 0:
            return -2

    else:
        return 0


print(mobiusFunction(25))
print(primeFactor(120))
