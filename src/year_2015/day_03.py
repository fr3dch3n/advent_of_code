from src.utils import read_input


def walk(pos: (int, int), instruction: str) -> (int, int):
    if instruction == "<":
        return pos[0] - 1, pos[1]
    if instruction == ">":
        return pos[0] + 1, pos[1]
    if instruction == "^":
        return pos[0], pos[1] + 1
    if instruction == "v":
        return pos[0], pos[1] - 1


def house_with_at_least_one_present(instructions: str) -> list[(int, int)]:
    start = (0, 0)
    current_pos = start
    visited_houses = [start]
    for instruction in instructions:
        new_pos = walk(current_pos, instruction)
        visited_houses.append(new_pos)
        current_pos = new_pos
    return visited_houses


def solution_a() -> int:
    lines = read_input(2015, 3)
    return len(set(house_with_at_least_one_present(lines[0].strip())))


def solution_b() -> int:
    lines = read_input(2015, 3)
    list1 = lines[0].strip()[::2]  # Every second item starting from index 0
    list2 = lines[0].strip()[1::2]
    return len(
        set(
            house_with_at_least_one_present(list1)
            + house_with_at_least_one_present(list2)
        )
    )
