def binaryRecursive(decimal: int) -> str:
    decimal = int(decimal)
    if decimal in (0, 1):
        return str(decimal)
    div, mod = divmod(decimal, 2)
    return binaryRecursive(div) + str(mod)


def main(number: str) -> str:
    number = str(number).strip()
    if not number:
        raise ValueError("no input was provided")
    negative = "-" if number.startswith("-") else ""
    number = number.lstrip("-")
    if not number.isnumeric():
        raise ValueError("input value must integer")
    return f"{negative} 0b{binaryRecursive(int(number))}"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
