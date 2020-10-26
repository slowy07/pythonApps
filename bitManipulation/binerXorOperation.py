
def binaryXor(a: int, b: int):
    if a < 0 or b < 0:
        raise Exception("input must integer positive")

    aBinary = str(bin(a))[2:]
    bBinary = str(bin(b))[2:]
    maxLength = max(len(aBinary), len(bBinary))

    return "0b" + "".join(
        str(int(char_a != char_b))
        for charA, charB in zip(aBinary.zfill(maxLength), bBinary.zfill(maxLength))
    )

if __name__ == '__main__':
    import doctest
    doctest.main()
