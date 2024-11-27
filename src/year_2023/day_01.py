from src.utils import read_input


def calibration_value(input: str) -> int:
    digits: list[int] = [int(i) for i in input if i.isdigit()]
    return digits[0] * 10 + digits[-1]


def nouns_calibration_value(input: str) -> int:
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    r = ""
    for i in range(len(input)):
        for idx, val in enumerate(mappings, 1):
            if input[i:].startswith(val):
                r += str(idx)
            else:
                r += input[i]

    return calibration_value(r)


def solution_a():
    lines = read_input(2023, 1)
    return sum([calibration_value(l) for l in lines])


def solution_b():
    lines = read_input(2023, 1)
    return sum([nouns_calibration_value(l) for l in lines])
