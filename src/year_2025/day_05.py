def is_ingredient_spoiled(ingredient, ranges):
    for left, right in ranges:
        if ingredient >= left and ingredient <= right:
            return True
    return False


def how_many_ingredients_are_spoiled(ingredients, ranges):
    return len([n for n in ingredients if is_ingredient_spoiled(n, ranges)])


def how_many_fresh_ingredients(ranges):
    ranges = sorted(ranges)
    first = ranges[0]
    s = first[1] - first[0] + 1
    end = first[1]
    for left, right in ranges[1:]:
        if left > end:
            s += right - left + 1
        else:
            s += max(0, right - end)
        end = max(end, right)
    return s


def parse_input(lines):
    i = lines.index("\n")
    ranges = []
    for n in lines[:i]:
        p = n.split("-")
        ranges.append([int(p[0]), int(p[1])])

    ingredients = list(map(int, lines[i + 1 :]))
    return ingredients, ranges


def solution_a():
    with open("src/year_2025/day_05.txt") as f:
        lines = [s for s in f.readlines()]
        ingredients, ranges = parse_input(lines)
        return how_many_ingredients_are_spoiled(ingredients, ranges)


def solution_b():
    with open("src/year_2025/day_05.txt") as f:
        lines = [s for s in f.readlines()]
        _, ranges = parse_input(lines)
        return how_many_fresh_ingredients(ranges)
