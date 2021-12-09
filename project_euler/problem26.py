def solution(numerator: int = 1, digit: int = 1000) -> int:
    the_digit = 1
    longlest_list_length = 0

    for diviide_by_number in range(numerator, digit + 1):
        has_been_divided: list[int] = []
        now_divide = numerator

        for division_cycle in range(1, digit + 1):
            if now_divide in has_been_divided:
                if longlest_list_length < len(has_been_divided):
                    longlest_list_length = len(has_been_divided)
                    the_digit = diviide_by_number

            else:
                has_been_divided.append(now_divide)
                now_divide = now_divide * 10 % diviide_by_number

    return the_digit


print(solution(10, 1000))
