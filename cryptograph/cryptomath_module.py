def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def find_mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None

    u1 = 1
    u2 = 0
    u3 = a

    v1 = 0
    v2 = 1
    v3 = m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
