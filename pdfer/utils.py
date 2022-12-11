from pathlib import Path
import random
import string

OUTPUT_PATH = Path().cwd() / "output"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def get_random_name():
    return "".join(random.choices(string.ascii_letters, k=6))
