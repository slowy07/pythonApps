def solution() -> int:
    """Returns
    >>> solution()
    210
    """
    constant = []
    i = 1

    while len(constant) < 1e6:
        constant.append(str(i))
        i += 1

    constant = "".join(constant)

    return (
        int(constant[0])
        * int(constant[9])
        * int(constant[99])
        * int(constant[999])
        * int(constant[9999])
        * int(constant[99999])
        * int(constant[999999])
    )


if __name__ == "__main__":
    print(solution())
