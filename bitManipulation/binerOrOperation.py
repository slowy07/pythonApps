def binaryOr(a: int, b:int):
    if a < 0 or b < 0:
        raise Exception("input must integer positive")
    aBinary = str(bin(a))[2:]
    bBinary = str(bin(b))[2:]
    maxLength = max(len(aBinary), len(bBinary))

    return "0b"+"".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(aBinary.zfill(maxLength), bBinary.zfill(bBinary))
    )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
