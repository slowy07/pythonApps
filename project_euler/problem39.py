from __future__ import annotations

import typing
from collections import Counter


def pythagorean_triple(max_perimeter: int) -> typing.Counter[int]:
    triplets: typing.Counter[int] = Counter()
    for base in range(1, max_perimeter + 1):
        for perpendicular in range(base, max_perimeter + 1):
            hypotenuse = (base * base + perpendicular * perpendicular) ** 0.5
            if hypotenuse == int(hypotenuse):
                perimeter = int(base + perpendicular + hypotenuse)
                if perimeter > max_perimeter:
                    continue
                triplets[perimeter] += 1

    return triplets


def solution(n: int = 1000) -> int:
    triplets = pythagorean_triple(n)
    return triplets.most_common(1)[0][0]


if __name__ == "__main__":
    print(solution())
