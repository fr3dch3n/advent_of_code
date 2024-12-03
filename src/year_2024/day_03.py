import re

from src.utils import read_input


def sum_all_muls(lines: list[str]) -> int:
    sum = 0

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in lines:
        matches = re.findall(pattern, line)
        for m in matches:
            sum += int(m[0]) * int(m[1])

    return sum


def sum_all_enabled_muls(lines: list[str]) -> int:
    sum = 0

    mul_active = True

    pattern = r"""mul\((\d{1,3}),(\d{1,3})\)|(do(?:n't)?)\(\)"""
    for line in lines:
        matches = re.findall(pattern, line)
        for m in matches:
            if m[2] == "do":
                mul_active = True
            if m[2] == "don't":
                mul_active = False
            if mul_active:
                ints = []
                for n in m:
                    try:
                        ints.append(int(n))
                    except:
                        pass
                if len(ints) == 2:
                    sum += ints[0] * ints[1]
    return sum


def solution_a():
    lines = read_input(2024, 3)
    return sum_all_muls(lines)


def solution_b():
    lines = read_input(2024, 3)
    return sum_all_enabled_muls(lines)
