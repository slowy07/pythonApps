from __future__ import annotations


def is_9_pandigital(n: int) -> bool:
    s = str(n)
    return len(s) == 9 and set(s) == set("123456789")


def solution() -> int | None:
    for base_num in range(9999, 99, -1):
        candidate = 100002 * base_num
        if is_9_pandigital(candidate):
            return candidate

    for base_num in range(333, 99, -1):
        candidate = 1002003 * base_num
        if is_9_pandigital(candidate):
            return candidate

    return None


if __name__ == "__main__":
    print(solution())
