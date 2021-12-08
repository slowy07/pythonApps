def octalToDecimal(octString: str) -> str:
    octString = str(octString).strip()
    if not octString:
        raise ValueError("empty string was passed to function")
    isNegative = octString[0] == "-"
    if isNegative:
        octString = octString[1:]
    if not all(0 <= int(char) <= 7 for char in octString):
        raise ValueError("non octal value was passed to function")
    decimalNumber = 0
    for char in octString:
        decimalNumber = 8 * decimalNumber + int(char)
    if isNegative:
        decimalNumber = -decimalNumber

    return decimalNumber


if __name__ == "__main__":
    from doctest import testmod

    testmod()
