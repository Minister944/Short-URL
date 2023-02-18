import random


def random_str(length: int = 8):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    short_key = "".join(random.choice(chars) for _ in range(length))
    return short_key
