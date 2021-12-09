def solution(n: int = 100) -> int:
    collect_power = set()
    current_power = 0
    N = n + 1

    for a in range(2, N):
        for b in range(2, N):
            current_power = a ** b
            collect_power.add(current_power)

    return len(collect_power)


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
