values = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


def decimalToHexadecimal(decimal):
    assert type(decimal) in (int, float) and decimal == int(decimal)
    hexadecimal = ""
    negative = False
    if decimal < 0:
        negative = True
        decimal *= -1
    while decimal > 0:
        decimal, remainder = divmod(decimal, 16)
        hexadecimal = values[remainder] + hexadecimal
    hexadecimal = "0x" + hexadecimal
    if negative:
        hexadecimal = "-" + hexadecimal
    return hexadecimal


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(decimalToHexadecimal(2))
