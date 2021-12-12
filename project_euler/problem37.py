from __future__ import annotations

sieve = [True] * 1000001
sieve[1] = False

i = 2
while i * i <= 1000001:
    if sieve[i]:
        for j in range(i * i, 1000001, i):
            sieve[j] = False

    i += 1


def is_prime(n: int) -> bool:
    return sieve[n]


def list_truncated_nums(n: int) -> list[int]:
    str_num = str(n)
    list_num = [n]
    for i in range(1, len(str_num)):
        list_num.append(int(str_num[i:]))
        list_num.append(int(str_num[:-i]))

    return list_num


def validate(n: int) -> bool:
    if len(str(n)) > 3:
        if not is_prime(int(str(n)[-3:])) or not is_prime(int(str(n)[:3])):
            return False

    return True


def compute_truncated_prime(count: int = 11) -> list[int]:
    list_truncated_primes: list[int] = []
    num = 13
    while len(list_truncated_primes) != count:
        if validate(num):
            list_num = list_truncated_nums(num)
            if all(is_prime(i) for i in list_num):
                list_truncated_primes.append(num)

        num += 2

    return list_truncated_primes


def solution() -> int:
    return sum(compute_truncated_prime(11))


print(solution())


print(is_prime(87))
