from math import ceil


def solution(n: int = 1001) -> int:
    total = 1

    for i in range(1, int(ceil(n / 2.0))):
        odd = 2 * i + 1
        even = 2 * i
        total = total + 4 * odd ** 2 - 6 * even

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(solution())
    else:
        try:
            n = int(sys.argv[1])
            print(solution(n))
        except ValueError:
            print("err")
