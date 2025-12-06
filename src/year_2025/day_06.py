import math


def parse_input(lines: list[str]) -> list[list[str]]:
    separator_columns = []
    total_length = len(lines[0])
    for c in range(total_length):
        all_spaces = True
        for r in lines:
            if r[c] != " ":
                all_spaces = False
                break
        if all_spaces:
            separator_columns.append(c)

    problems = []
    separator_column_idx = 0
    next_separator = separator_columns[separator_column_idx]
    for line in lines:
        next_element = ""
        for i, c in enumerate(line):
            if i < next_separator:
                next_element += c

                if i == len(line) - 1:
                    if separator_column_idx >= len(problems):
                        problems.append([next_element.replace("\n", "")])
                    else:
                        problems[separator_column_idx].append(next_element.replace("\n", ""))
            else:
                if separator_column_idx >= len(problems):
                    problems.append([next_element.replace("\n", "")])
                else:
                    problems[separator_column_idx].append(next_element.replace("\n", ""))

                next_element = ""
                separator_column_idx += 1
                if separator_column_idx >= len(separator_columns):
                    next_separator = len(line)
                else:
                    next_separator = separator_columns[separator_column_idx]
        separator_column_idx = 0
        next_separator = separator_columns[separator_column_idx]
    return problems


def map_to_from_right(problems: list[list[str]]) -> list[list[str]]:
    mapped_problems = []
    for problem in problems:
        intermediate_problem = []
        col_width = max([len(n) for n in problem])
        for i in range(col_width - 1, -1, -1):
            intermediate_number = ""
            for n in problem[:-1]:
                intermediate_number += n[i]
            intermediate_problem.append(intermediate_number)
        intermediate_problem.append(problem[-1])
        mapped_problems.append(intermediate_problem)
    return [[y.strip() for y in x] for x in mapped_problems]


def grand_total(problems: list[list[str]], mapping_fn=None) -> int:
    if mapping_fn:
        problems = mapping_fn(problems)
    gt = 0
    for p in problems:
        ns = [int(n.strip()) for n in p[:-1]]
        if p[-1].strip() == "+":
            gt += sum(ns)
        elif p[-1].strip() == "*":
            gt += math.prod(ns)
    return gt


def solution_a():
    with open("src/year_2025/day_06.txt") as f:
        lines = [s for s in f.readlines()]
        input = parse_input(lines)
        return grand_total(input)


def solution_b():
    with open("src/year_2025/day_06.txt") as f:
        lines = [s for s in f.readlines()]
        input = parse_input(lines)
        return grand_total(input, map_to_from_right)
