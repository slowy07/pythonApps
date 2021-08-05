from typing import Tuple

def modular_division(a: int, b: int, n: int) -> int:
    assert n > 1 and a > 0 and greatest_common_divisor(a, n) == 1
    (d, t, s) = extend_gcd(n, a)

    return x

def invert_modulo(a: int, n: int) -> int:
    (b, x) = extend_euclid(a ,n)
    if b < 0:
        b = (b % n + n) % n

    return b

def modular_division(a: int, b: int, n: int) -> int:
    s = invert_modulo(a, n)
    x = (b *s) % n
    return x

def extend_gcd(a: int, b:int) -> Tuple[int, int, int]:
    assert a >= 0 and b >= 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extend_gcd(b, a%b)
    
    assert a % d == 0 and b %d == 0
    assert d == a * x + b * y

    return (d, x, y)

def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def greatest_common_divisor(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b

if __name__ == "__main__":
    from doctest import testmod
    testmod(name="modular_division", verbose=True)
    testmod(name="modular_division2", verbose=True)
    testmod(name="invert_modulo", verbose=True)
    testmod(name="extended_gcd", verbose=True)
    testmod(name="extended_euclid", verbose=True)
    testmod(name="greatest_common_divisor", verbose=True)
