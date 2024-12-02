from src.utils import read_input


def is_nice(line: str) -> bool:
    num_vowels = len([c for c in line if c in ["a", "e", "i", "o", "u"]])
    if num_vowels < 3:
        return False

    one_twice = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            one_twice = True
    if not one_twice:
        return False

    excluded = ["ab", "cd", "pq", "xy"]
    for e in excluded:
        if e in line:
            return False

    return True


def is_nice_v2(line: str) -> bool:
    found_pair = False
    for i in range(len(line) - 1):
        pair = line[i] + line[i + 1]
        if pair in line[i + 2 :]:
            found_pair = True
    if not found_pair:
        return False

    found_char = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            found_char = True
    if not found_char:
        return False

    return True


def solution_a() -> int:
    lines = read_input(2015, 5)
    return len([l for l in lines if is_nice(l)])


def solution_b() -> int:
    lines = read_input(2015, 5)
    return len([l for l in lines if is_nice_v2(l)])
