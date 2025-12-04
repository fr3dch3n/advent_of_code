def count_neighbors(grid, row, col, target):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, 0),  # up
        (-1, 1),  # up-right
        (0, 1),  # right
        (1, 1),  # down-right
        (1, 0),  # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1),  # up-left
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            if grid[r][c] == target:
                count += 1

    return count


def which_rolls_can_be_accessed(input: list[list[str]]) -> int:
    position_accessible = []
    for row_idx, row in enumerate(input):
        for col_idx, cell in enumerate(row):
            if cell == "@":
                neighbours = count_neighbors(input, row_idx, col_idx, "@")
                if neighbours < 4:
                    position_accessible.append((row_idx, col_idx))
    return position_accessible


def how_many_rolls_in_total_can_be_accessed(input: list[list[str]]) -> int:
    total = 0
    accessible_positions = which_rolls_can_be_accessed(input)
    total += len(accessible_positions)
    while len(accessible_positions) > 0:
        for row_idx, col_idx in accessible_positions:
            input[row_idx][col_idx] = "x"
        accessible_positions = which_rolls_can_be_accessed(input)
        total += len(accessible_positions)
    return total


def solution_a():
    with open("src/year_2025/day_04.txt") as f:
        lines = [list(s) for s in f.readlines()]
        return len(which_rolls_can_be_accessed(lines))


def solution_b():
    with open("src/year_2025/day_04.txt") as f:
        lines = [list(s) for s in f.readlines()]
        return how_many_rolls_in_total_can_be_accessed(lines)
