import string
import random

CHARACTER_CHOICES = string.ascii_uppercase + string.digits + string.ascii_lowercase


def random_character_generator(size=10, chars=CHARACTER_CHOICES):
    return f"{''.join(random.choice(chars) for _ in range(size))}\n"


def random_integer_generator(size=5):
    range_start = 10 ** (size - 1)
    range_end = (10 ** size) - 1
    return f"{random.randint(range_start, range_end)}\n"
