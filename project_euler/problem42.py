import os

TRINAGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)]


def solution() -> int:

    script_dir = os.path.dirname(os.path.realpath(__file__))
    wordFilePath = os.path.join(script_dir, "input_file/problem42.txt")
    words = ""
    with open(wordFilePath) as f:
        words = f.readline()

    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(",")))
    words = list(
        filter(
            lambda word: word in TRINAGULAR_NUMBERS,
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words),
        )
    )
    return len(words)


if __name__ == "__main__":
    print(solution())
