from src.utils import read_input


def is_report_safe(report: list[int]) -> bool:
    decreasing = False
    if report[0] > report[1]:
        decreasing = True
    for i, value in enumerate(report):
        if i > 0:
            if decreasing and report[i] > report[i - 1]:
                return False
            if not decreasing and report[i] < report[i - 1]:
                return False
            diff = abs(report[i] - report[i - 1])
            if diff < 1 or diff > 3:
                return False
    return True


def problem_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        modified_list = report[:i] + report[i + 1 :]
        if is_report_safe(modified_list):
            return True
    return False


def sum_safe_reports(input: list[str]) -> int:
    return sum([is_report_safe([int(x) for x in i.split()]) for i in input])


def sum_problem_dampener(input: list[str]) -> int:
    return sum([problem_dampener([int(x) for x in i.split()]) for i in input])


def solution_a():
    lines = read_input(2024, 2)
    return sum_safe_reports(lines)


def solution_b():
    lines = read_input(2024, 2)
    return sum_problem_dampener(lines)
