from __future__ import annotations

sieve = [True] * 1000001
i = 2
while i * i <= 1000000:
    if sieve[i]:
        for j in range(i * i, 1000001, i):
            sieve[j] = False

    i += 1


def is_prime(n: int) -> bool:
    return sieve[n]


def contains_an_even_digit(n: int) -> bool:
    return any(digit in "02468" for digit in str(n))


def find_circular_prime(limit: int = 1000000) -> list[int]:
    result = [2]
    for num in range(3, limit + 1, 2):
        if is_prime(num) and not contains_an_even_digit(num):
            str_num = str(num)
            list_nums = [int(str_num[j:] + str_num[:j]) for j in range(len(str_num))]
            if all(is_prime(i) for i in list_nums):
                result.append(num)

    return result


def solution() -> int:
    return len(find_circular_prime(1000000))


if __name__ == "__main__":
    print(solution())
