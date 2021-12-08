#  0 3 4 5 4 3


def solution(n: int = 1000) -> int:
    one_count = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens_count = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

    count = 0

    for i in range(1, n + 1):
        if i < 1000:
            if i >= 100:
                count += one_count[i // 100] + 7

                if i % 100 != 0:
                    count += 3
            if 0 < i % 100 < 20:
                count += one_count[i % 100]
            else:
                count += one_count[i % 10]
                count += tens_count[(i % 100 - i % 10) // 10]

        else:
            count += one_count[i // 1000] + 8

    return count


if __name__ == "__main__":
    print(solution())

    # n = 19
    # n = 342 32 115 * (s) = 21124
