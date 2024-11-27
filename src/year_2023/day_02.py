from src.utils import read_input


def parse_input(line: str) -> (int, list[dict[str, int]]):
    parts = line.split(": ")
    id = parts[0].strip().split("Game ")
    raw_sets = parts[1].split(";")
    new_sets = []
    for raw_set in raw_sets:
        s = {}
        for c in raw_set.split(", "):
            x = c.strip().split(" ")
            s[x[1]] = int(x[0].strip())
        new_sets.append(s)
    return int(id[1]), new_sets


def game_possible(game: list[dict[str, int]], nrs: dict[str, int]) -> bool:
    max_per_color = calc_max_per_game(game)

    would_fit = True
    for c, n in nrs.items():
        if c not in max_per_color or max_per_color[c] > n:
            would_fit = False

    return would_fit


def calc_max_per_game(game: list[dict[str, int]]) -> dict[str, int]:
    max_per_color = {}
    for game_set in game:
        for k, v in game_set.items():
            if k in max_per_color:
                if v > max_per_color[k]:
                    max_per_color[k] = v
            else:
                max_per_color[k] = v
    return max_per_color


def minimal_set_power(game: list[dict[str, int]]) -> int:
    max_per_color = calc_max_per_game(game)
    n = 1
    for k, v in max_per_color.items():
        n *= v
    return n


def sum_minimal_set_power(input: list[str]) -> int:
    s = 0
    for i in input:
        id, g = parse_input(i)
        s += minimal_set_power(g)
    return s


def sum_of_possible_games(input: list[str], nrs: dict[str, int]) -> int:
    s = 0
    for i in input:
        id, g = parse_input(i)
        if game_possible(g, nrs):
            s += id
    return s


def solution_a():
    lines = read_input(2023, 2)
    return sum_of_possible_games(lines, {"red": 12, "green": 13, "blue": 14})


def solution_b():
    lines = read_input(2023, 2)
    return sum_minimal_set_power(lines)
