from src.utils import read_input


def count_mas(lines: list[str]) -> int:
    a_positions = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                a_positions.append((x, y))

    count = 0
    for x in a_positions:
        count += check_x_shape_mas(lines, x)

    return count


def check_x_shape_mas(lines: list[str], middle: (int, int)) -> int:
    x, y = middle
    if x == 0 or x == len(lines[0]) - 1 or y == 0 or y == len(lines) - 1:
        return False

    top_right = lines[y - 1][x + 1]
    top_left = lines[y - 1][x - 1]
    bottom_right = lines[y + 1][x + 1]
    bottom_left = lines[y + 1][x - 1]

    if (
        top_left == "M"
        and bottom_right == "S"
        and top_right == "M"
        and bottom_left == "S"
    ):
        return True

    if (
        top_left == "S"
        and bottom_right == "M"
        and top_right == "S"
        and bottom_left == "M"
    ):
        return True

    if (
        top_left == "S"
        and bottom_right == "M"
        and top_right == "M"
        and bottom_left == "S"
    ):
        return True

    if (
        top_left == "M"
        and bottom_right == "S"
        and top_right == "S"
        and bottom_left == "M"
    ):
        return True

    return False


def count_xmas(lines: list[str]) -> int:
    x_positions = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "X":
                x_positions.append((x, y))

    count = 0
    for x in x_positions:
        count += check_xmas(lines, x)

    return count


def check_xmas(lines: list[str], pos: (int, int)) -> int:
    check_direction_partial = lambda x_fn, y_fn: check_direction(
        lines, ["M", "A", "S"], [1, 2, 3], pos, x_fn, y_fn
    )

    count = 0
    count += check_direction_partial(lambda i, k: i + k, lambda j, k: j)  # check right
    count += check_direction_partial(lambda i, k: i, lambda j, k: j + k)  # check down
    count += check_direction_partial(
        lambda i, k: i + k, lambda j, k: j + k
    )  # check diagonal down right
    count += check_direction_partial(
        lambda i, k: i - k, lambda j, k: j + k
    )  # check diagonal down left
    count += check_direction_partial(lambda i, k: i, lambda j, k: j - k)  # check up
    count += check_direction_partial(
        lambda i, k: i + k, lambda j, k: j - k
    )  # check diagonal up right
    count += check_direction_partial(
        lambda i, k: i - k, lambda j, k: j - k
    )  # check diagonal up left
    count += check_direction_partial(lambda i, k: i - k, lambda j, k: j)  # check left
    return count


def check_direction(
    lines: list[str], chars, offsets, pos: (int, int), x_fn, y_fn
) -> int:
    count = 0
    x, y = pos
    for k in zip(chars, offsets):
        next_x = x_fn(x, k[1])
        next_y = y_fn(y, k[1])
        if 0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines):
            if lines[next_y][next_x] == k[0]:
                count += 1
    return count == 3


def solution_a():
    lines = read_input(2024, 4)
    return count_xmas(lines)


def solution_b():
    lines = read_input(2024, 4)
    return count_mas(lines)
