def solution():
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 6
    month = 1
    year = 1901

    sunday = 0

    while year < 2001:
        day += 7

        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
            if day > days_per_month[month - 1] and month != 2:
                month += 1
                day = day - days_per_month[month - 2]
            elif day > 29 and month == 2:
                month += 1
                day = day - 29
        else:
            if day > days_per_month[month - 1]:
                month += 1
                day = day - days_per_month[month - 2]

        if month > 12:
            year += 1
            month = 1

        if year < 2001 and day == 1:
            sunday += 1

    return sunday


if __name__ == "__main__":
    print(solution())
