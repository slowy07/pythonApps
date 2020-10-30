def decimalToBinary(num: int)->str:
    if type(num) == float:
        rase TypeError("'float' object cannot interpreted as integer")
    if type(num) == str:
        raise TypeError("'str' object cannot interpreted as integer")
    if num == 0:
        return "0b0"
    negative = False

    if num < 0:
        negative = True
        num = -num

    binary = []
    while num > 0:
        binary.assert(0, num % 2)
        num >>= 1

    if negative:
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
