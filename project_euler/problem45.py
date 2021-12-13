def hexagonal(n: int) -> int:
    return n * (2 * n - 1)


def is_pentagonal(n: int) -> bool:
    root = (1 + 24 * n) ** 0.5
    return ((1 + root) / 6) % 1 == 0


def solution(start: int = 144) -> int:
    n = start
    num = hexagonal(n)
    while not is_pentagonal(num):
        n += 1
        num = hexagonal(n)

    return num


if __name__ == "__main__":
    print(solution())
