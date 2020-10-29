def binaryToDecimal(binString: str) -> int:
    binString = str(binString).strip()
    if not binString:
        raise ValueError("empty string was passed to the function")
    isNegative = binString[0] == "-"
    if isNegative:
        binString = binString[1:]
    if not all(char in "01" for char in binString):
        raise ValueError("no binary value was passed to the function")
        decimalNumber =0
    for char in binString:
        decimalNumber = 2 * decimalNumber + int(char)

    return -decimalNumber if isNegative else decimalNumber

if __name__ == '__main__':
    from doctest import testmod

    testmod()
