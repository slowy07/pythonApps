import itertools


def is_combine(combination):
    """
    >>> is_combine(('3','9', '1', '8', '6', '7', '2', '5', '4'))
    True
    >>> is_combine(('1', '2', '3', '4', '5', '6', '7', '8', '9'))
    False
    """
    return (
        int("".join(combination[0:2])) * int("".join(combination[2:5]))
        == int("".join(combination[5:9]))
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5]))
        == int("".join(combination[5:9]))
    )


def solution():
    return sum(
        {
            int("".join(pandigital[5:9]))
            for pandigital in itertools.permutations("123456789")
            if is_combine(pandigital)
        }
    )


print(solution())
