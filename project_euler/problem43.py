from itertools import permutations


def is_substring_divisible(num: tuple) -> bool:
    if num[3] % 2 != 0:
        return False

    if (num[2] + num[3] + num[4]) % 3 != 0:
        return False

    if num[5] % 5 != 0:
        return False

    tests = [7, 11, 13, 17]
    for i, test in enumerate(tests):
        if (num[i + 4] * 100 + num[i + 5] * 10 + num[i + 6]) % test != 0:
            return False

    return True


def solution(n: int = 10) -> int:
    return sum(
        int("".join(map(str, num)))
        for num in permutations(range(n))
        if is_substring_divisible(num)
    )


if __name__ == "__main__":
    print(solution())
