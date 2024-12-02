from src.utils import read_raw_input


def count_string(line: str) -> int:
    return len(line) - len(eval(line))


def count_string_v2(line: str) -> int:
    return line.count("\\") + line.count('"') + 2


def solution_a() -> int:
    lines = read_raw_input(2015, 8)
    return sum([count_string(l) for l in lines])


def solution_b() -> int:
    lines = read_raw_input(2015, 8)
    return sum([count_string_v2(l) for l in lines])
