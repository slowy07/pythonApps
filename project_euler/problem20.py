def factorial(angka: int) -> int:
    fact = 1
    for i in range(1, angka + 1):
        fact *= i
    return fact


def split_add(angka: int) -> int:
    sum_of_digit = 0
    while angka > 0:
        last_digit = angka % 10
        sum_of_digit += last_digit
        angka = angka // 10

    return sum_of_digit


def solution(angka: int = 100) -> int:
    nfact = factorial(angka)
    res = split_add(nfact)
    return res


if __name__ == "__main__":
    print(solution())
