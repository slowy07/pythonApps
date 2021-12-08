def binaryAnd(a: int, b: int) -> str:
    if a < 0 and b < 0:
        raise ValueError("the value integer mus be positive")

    aBinary = str(bin(a))[2:]
    bBinary = str(bin(b))[2:]
    maxLength = max(len(aBinary), len(bBinary))

    return "0b" + "".join(
        str(int(char_a == "1" and char_b == "1"))
        for char_a, char_b in zip(aBinary.zfill(maxLength), bBinary.zfill(maxLength))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
