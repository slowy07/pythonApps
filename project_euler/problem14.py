def solution(n: int = 1000000) -> int:
    largest_number = 1
    pre_counter = 1
    counters = {1: 1}

    for input1 in range(2, n):
        counter = 0
        number = input1

        while True:
            if number in counters:
                counter += counters[number]
                break
            if number % 2 == 0:
                number //= 2
                counter += 1
            else:
                number = (3 * number) + 1
                counter += 1

        if input1 not in counters:
            counters[input1] = counter

        if counter > pre_counter:
            largest_number = input1
            pre_counter = counter

    return largest_number


if __name__ == "__main__":
    print(solution(int(input().strip())))
