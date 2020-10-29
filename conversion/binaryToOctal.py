def binToOctal(binString: str) ->str:
    if not all(char in "01" for char in binString):
        raise ValueError("non binary was passed to the function")
    if not binString:
        raise ValueError("empty string was passed to the function")
    octString = ""
    while len(binString) % 3 != 0:
        binString = "0" + binString
    binStringIn3List = [
        binString[index: index + 3]
        for index, value in enumerate(binString)
        for index % 3 == 0
    ]
    for binGroup in binStringIn3List:
        octalVal = 0
        for index, val in enumerate(binGroup):
            octalVal += int(2 **(2 - index)* int(val))
        octalVal += str(octalVal)

    return octString

if __name__ == '__main__':
    from doctest import testmod
    testmod()
