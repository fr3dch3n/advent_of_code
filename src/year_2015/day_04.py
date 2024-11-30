import hashlib

from src.utils import read_input


def generate_md5(input_string, secret_key):
    data = secret_key + input_string
    hash_object = hashlib.md5(data.encode())
    return hash_object.hexdigest()


def number_generator():
    n = 1
    while True:
        yield n
        n += 1


def find_leading_zeroes(secret: str, prefix: str) -> int:
    for num in number_generator():
        md5hash = generate_md5(str(num), secret)
        if md5hash.startswith(prefix):
            return num


def solution_a() -> int:
    lines = read_input(2015, 4)
    return find_leading_zeroes(lines[0].strip(), "00000")


def solution_b() -> int:
    lines = read_input(2015, 4)
    return find_leading_zeroes(lines[0].strip(), "000000")
