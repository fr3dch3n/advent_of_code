from src.utils import read_input
from multiprocessing import Pool


def distinct_guard_positions(lines: list[str]) -> set[(int, int)]:
    max_y = len(lines)
    max_x = len(lines[0])

    positions = set()
    obstacles = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                positions.add((x, y))
    current_guard_position = positions.pop()
    current_facing_direction = "up"

    next_pos = next_position(current_guard_position, current_facing_direction)
    while max_x > next_pos[0] >= 0 and max_y > next_pos[1] >= 0:
        if next_pos in obstacles:
            current_facing_direction = turn_right(current_facing_direction)
        else:
            current_guard_position = next_pos
            positions.add(current_guard_position)
        next_pos = next_position(current_guard_position, current_facing_direction)

    return positions


def is_a_loop(
    start_position: (int, int),
    start_direction: str,
    obstacles: set[(int, int)],
    max_x: int,
    max_y: int,
) -> bool:
    positions_visited = [{start_position: start_direction}]

    current_guard_position = start_position
    current_facing_direction = start_direction
    next_pos = next_position(current_guard_position, current_facing_direction)
    while max_x > next_pos[0] >= 0 and max_y > next_pos[1] >= 0:
        if next_pos in obstacles:
            current_facing_direction = turn_right(current_facing_direction)
        else:
            current_guard_position = next_pos
            if {current_guard_position: current_facing_direction} in positions_visited:
                return True
            else:
                positions_visited.append(
                    {current_guard_position: current_facing_direction}
                )
        next_pos = next_position(current_guard_position, current_facing_direction)

    return False


def number_of_obstacles_to_create_loop(lines: list[str]) -> int:
    positions_to_check = distinct_guard_positions(lines)

    max_y = len(lines)
    max_x = len(lines[0])

    positions = set()
    obstacles = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                positions.add((x, y))

    current_guard_position = positions.pop()
    current_facing_direction = "up"

    positions_to_check.remove(current_guard_position)

    pool = Pool(processes=8)
    count_checked = 0

    results = []
    for position_to_check in positions_to_check:
        obstacles_with_adjustment = obstacles.copy()
        obstacles_with_adjustment.add(position_to_check)
        results.append(
            pool.apply_async(
                is_a_loop,
                (
                    current_guard_position,
                    current_facing_direction,
                    obstacles_with_adjustment,
                    max_x,
                    max_y,
                ),
            )
        )

        count_checked += 1

    c = 0
    for result in results:
        if result.get():
            c += 1
    return c


def turn_right(current_direction):
    if current_direction == "up":
        return "right"
    elif current_direction == "right":
        return "down"
    elif current_direction == "down":
        return "left"
    elif current_direction == "left":
        return "up"
    else:
        raise ValueError("Invalid direction")


def next_position(current_pos, direction):
    if direction == "up":
        return (current_pos[0], current_pos[1] - 1)
    elif direction == "down":
        return (current_pos[0], current_pos[1] + 1)
    elif direction == "left":
        return (current_pos[0] - 1, current_pos[1])
    elif direction == "right":
        return (current_pos[0] + 1, current_pos[1])
    else:
        raise ValueError("Invalid direction")


def solution_a():
    lines = read_input(2024, 6)
    return len(distinct_guard_positions(lines))


def solution_b():
    lines = read_input(2024, 6)
    return number_of_obstacles_to_create_loop(lines)
