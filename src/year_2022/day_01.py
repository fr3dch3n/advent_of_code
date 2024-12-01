from src.utils import read_input


def group_strings(input_list):
    grouped = []
    temp = []

    for item in input_list:
        if item.strip():
            temp.append(int(item))
        else:
            if temp:
                grouped.append(temp)
            temp = []

    if temp:
        grouped.append(temp)

    return grouped


def find_elf_most_calories(input: list[str]) -> int:
    grouped = group_strings(input)
    return max([sum(g) for g in grouped])


def find_top_three_elves_most_calories(input: list[str]) -> int:
    grouped = group_strings(input)
    calories_per_elf = [sum(g) for g in grouped]
    calories_per_elf.sort(reverse=True)
    return sum(calories_per_elf[:3])


def solution_a():
    lines = read_input(2022, 1)
    return find_elf_most_calories(lines)


def solution_b():
    lines = read_input(2022, 1)
    return find_top_three_elves_most_calories(lines)
