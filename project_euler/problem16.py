def solution(pangkat: int = 1000) -> int:
    num = 2 ** pangkat
    string_num = str(num)
    list_num = list(string_num)
    sum_of_num = 0

    for i in list_num:
        sum_of_num += int(i)

    return sum_of_num


if __name__ == "__main__":
    pangkat = int(input().strip())
    print("2 ^", pangkat, "=", 2 ** pangkat)
    res = solution(pangkat)
    print(res)
