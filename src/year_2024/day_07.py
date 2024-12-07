from itertools import product
from multiprocessing import Pool

from src.utils import read_input


def evaluate_combinations(numbers, operators):
    n = len(numbers) - 1
    all_combinations = list(product(operators, repeat=n))

    results = set()
    expressions = []

    for combination in all_combinations:
        expression = str(numbers[0])
        for i, op in enumerate(combination):
            if op == "||":
                expression = str(eval(expression)) + str(numbers[i + 1])
            else:
                expression = "(" + expression + op + str(numbers[i + 1]) + ")"
        try:
            result = eval(expression)
            results.add(result)
            expressions.append(expression)
        except Exception as e:
            print(f"Error evaluating expression {expression}: {e}")

    return results, expressions


def is_possible_equation(line: str, operators: list[str]) -> bool:
    parts = line.split(":")
    result = int(parts[0])
    parts = parts[1].split()
    numbers = [int(part) for part in parts]

    results, expressions = evaluate_combinations(numbers, operators)
    return result in results


def sum_possible_equations(lines: list[str], operators: list[str]) -> int:
    total = 0
    pool = Pool(processes=8)

    results = []
    for line in lines:
        results.append(
            {pool.apply_async(is_possible_equation, args=(line, operators)): line}
        )
    for result in results:
        if list(result.keys())[0].get():
            total += int(list(result.values())[0].split(":")[0])
    return total


def solution_a():
    lines = read_input(2024, 7)
    return sum_possible_equations(lines, ["+", "*"])


def solution_b():
    lines = read_input(2024, 7)
    return sum_possible_equations(lines, ["+", "*", "||"])
