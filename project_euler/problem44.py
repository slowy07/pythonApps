def is_pentagonal(n: int) -> bool:
    root = (1 + 24 * n) ** 0.5
    return ((1 + root) / 6) % 1 == 0


def solution(limit: int = 5000) -> int:
    pentagonal_nums = [(i * (3 * i - 1)) // 2 for i in range(1, limit)]
    for i, pentagonal_i in enumerate(pentagonal_nums):
        for j in range(i, len(pentagonal_nums)):
            pentagonal_j = pentagonal_nums[j]
            a = pentagonal_i + pentagonal_j
            b = pentagonal_j - pentagonal_i
            if is_pentagonal(a) and is_pentagonal(b):
                return b

    return -1


if __name__ == "__main__":
    print(solution())
