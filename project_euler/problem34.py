from math import factorial

DIGIT_FACTORIAL = {str(d): factorial(d) for d in range(10)}


def sum_digit_factorial(n: int) -> int:
    return sum(DIGIT_FACTORIAL[d] for d in str(n))


def solution() -> int:
    limit = 7 * factorial(9) + 1
    return sum(i for i in range(3, limit) if sum_digit_factorial(i) == i)


if __name__ == "__main__":
    print(solution())
