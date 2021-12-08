def hexa_to_bin(hex_num: str) -> int:
    hex_num = hex_num.strip()
    if not hex_num:
        raise ValueError("No value wass passed the function")

    is_negative = hex_num[0] == "-"
    if is_negative:
        hex_num = hex_num[1:]

    try:
        int_num = int(hex_num, 16)
    except ValueError:
        raise ValueError("invalid value was passed the function")

    bin_str = ""
    while int_num > 0:
        bin_str = str(int_num % 2) + bin_str
        int_num >>= 1

    return int(("-" + bin_str) if is_negative else bin_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
