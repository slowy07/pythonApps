import random


def happy():
    happy_emoji = [
        "😀",
        "😃",
        "😄",
        "😁",
    ]
    return random.choice(happy_emoji)


def sad():
    sad_emoji = ["😞", "😔", "😟", "😕", "🙁", "☹️"]
    return random.choice(sad_emoji)
