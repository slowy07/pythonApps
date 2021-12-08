hexTable = {hex(i)[2:]: i for i in range(16)}


def hexToDecimal(hexString: str) -> str:
    hexString = hexString.strip().lower()
    if not hexString:
        raise ValueError("empty string was passed to the function")
    isNegative = hexString[0] == "-"
    if isNegative:
        hexString = hexString[1:]
    if not all(char in hexTable for char in hexString):
        raise ValueError("non hexadecimal value was passed in function")
    decimalNumber = 0
    for char in hexString:
        decimalNumber = 16 * decimalNumber + hexTable[char]
    return -decimalNumber if isNegative else decimalNumber


if __name__ == "__main__":
    from doctest import testmod

    testmod()
