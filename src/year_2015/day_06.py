import re

from src.utils import read_input


class Light:
    state = 0

    def toggle(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def turn_on(self):
        self.state = 1

    def turn_off(self):
        self.state = 0


class BrightnessControlledLight:
    state = 0

    def toggle(self):
        self.state += 2

    def turn_on(self):
        self.state += 1

    def turn_off(self):
        if self.state > 0:
            self.state -= 1


def generate_rectangle_coords(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    x_min, x_max = sorted([x1, x2])
    y_min, y_max = sorted([y1, y2])

    coords = [(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)]
    return coords


def apply_instructions(lines: list[str], c) -> dict:
    pattern = r"(\D+) (\d+),(\d+) through (\d+),(\d+)"
    grid = {}

    for line in lines:
        matches = re.findall(pattern, line)[0]
        cmd = matches[0]
        left_x = int(matches[1])
        left_y = int(matches[2])
        right_x = int(matches[3])
        right_y = int(matches[4])

        coords = generate_rectangle_coords((left_x, left_y), (right_x, right_y))
        for coord in coords:
            if coord not in grid:
                grid[coord] = c()
            if cmd == "turn on":
                grid[coord].turn_on()
            if cmd == "turn off":
                grid[coord].turn_off()
            if cmd == "toggle":
                grid[coord].toggle()

    return grid


def solution_a() -> int:
    lines = read_input(2015, 6)
    grid = apply_instructions(lines, Light)
    return sum([1 for k, v in grid.items() if v.state == 1])


def solution_b() -> int:
    lines = read_input(2015, 6)
    grid = apply_instructions(lines, BrightnessControlledLight)
    return sum([v.state for k, v in grid.items()])
