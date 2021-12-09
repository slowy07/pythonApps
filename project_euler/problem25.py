from typing import Generator


def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


def solution(n: int = 1000) -> int:
    ans = 1
    gen = fibonacci_generator()
    while len(str(next(gen))) < n:
        ans += 1

    return ans + 1


print(solution(int(str(input()).strip())))
