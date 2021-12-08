import os


def solution():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    triangle = os.path.join(file_dir, "problem18.txt")

    with open(triangle) as f:
        triangle = f.readlines()

    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle]
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if j != len(a[i - 1]):
                number1 = a[i - 1][j]
            else:
                number1 = 0
            if j > 0:
                number2 = a[i - 1][j - 1]
            else:
                number2 = 0

            a[i][j] += max(number1, number2)

    return max(a[-1])


if __name__ == "__main__":
    print(solution())
