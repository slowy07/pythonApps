def decimalToAll(num: int, base: int) ->str:
    if isinstance(num, float):
        raise TypeError("int() can't convert non-string with explicit base")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if isinstance(base, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if isinstance(base, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if base in (0, 1):
        raise ValueError("base must be >= 2")
    if base > 36:
        raise ValueError("base must be <= 36")
    # fmt: off
    ALPHABET_VALUES = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
                       '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
                       '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
                       '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
                       '34': 'Y', '35': 'Z'}
    # fmt: on
    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = num // base
        num = div
        if div == 0:
            return str(new_value[::-1])
        elif div == 1:
            new_value += str(div)
            return str(new_value[::-1])

    return new_value[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    for base in range(2, 37):
        for num in range(1000):
            assert int(decimalToAll(num, base), base) == num, (
                num,
                base,
                decimalToAll(num, base),
                int(decimalToAll(num, base), base),
            )
