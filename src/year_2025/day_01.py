def dial(position, instruction: str):
    direction = instruction[:1]
    amount = int(instruction[1:])
    zeros = 0
    for i in range(amount):
        position = dial_one(position, direction)
        if position == 0:
            zeros += 1
    return position, zeros


def dial_one(position, direction) -> int:
    if direction == "L":
        position -= 1
    if direction == "R":
        position += 1
    if position == -1:
        return 99
    elif position == 100:
        return 0
    else:
        return position


def how_often_ends_at_zero(instructions):
    pos = 50
    cnt = 0
    for ins in instructions:
        pos, _ = dial(pos, ins)
        if pos == 0:
            cnt += 1
    return cnt


def how_often_passed_zero(instructions):
    pos = 50
    total_zeros = 0
    for ins in instructions:
        pos, zeros = dial(pos, ins)
        total_zeros += zeros
    return total_zeros


def solution_a():
    with open("src/year_2025/day_01.txt") as f:
        lines = [line.rstrip() for line in f]
        return how_often_ends_at_zero(lines)


def solution_b():
    with open("src/year_2025/day_01.txt") as f:
        lines = [line.rstrip() for line in f]
        return how_often_passed_zero(lines)
