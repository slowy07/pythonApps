def solution(limit=28123) -> int:
    sum_div = [1] * (limit + 1)

    for i in range(2, int(limit ** 0.5) + 1):
        sum_div[i * i] += i
        for k in range(i + 1, limit // i + 1):
            sum_div[k * i] += k + i

    abd = set()
    res = 0

    for n in range(1, limit + 1):
        if sum_div[n] > n:
            abd.add(n)

        if not any((n - a in abd) for a in abd):
            res += n

    return res


if __name__ == "__main__":
    print(solution())
