from src.utils import read_input


def floor_exit(instructions: str) -> int:
    return instructions.count("(") - instructions.count(")")


def entering_basement(instructions: str) -> int:
    floor = 0
    for idx, i in enumerate(instructions):
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        else:
            raise f"Unknown character: {i}"
        if floor == -1:
            return idx + 1
    raise "Shouldn't have reached this point"


def solution_a() -> int:
    lines = read_input(2015, 1)
    return floor_exit(lines[0])


def solution_b() -> int:
    lines = read_input(2015, 1)
    return entering_basement(lines[0])
