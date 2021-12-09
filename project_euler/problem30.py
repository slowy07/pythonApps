def solution_digit(s: str) -> int:
    i = sum(pow(int(c), 5) for c in s)
    return i if i == int(s) else 0


def solution() -> int:
    return sum(solution_digit(str(i)) for i in range(1000, 1000000))


if __name__ == "__main__":
    print(solution())
