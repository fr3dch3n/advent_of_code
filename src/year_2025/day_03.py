def max_joltage_of_battery_bank(input: str, nr_of_required_battiers: int) -> int:
    return __max_joltage_of_battery_bank_recursive(
        [int(c) for c in list(input)], [], nr_of_required_battiers
    )


def __max_joltage_of_battery_bank_recursive(
    inputs: list[int], current_build: list[int], missing_nr_of_batteries: int
):
    if missing_nr_of_batteries == 0:
        return int("".join([str(x) for x in current_build]))
    next_biggest_int = max(inputs[: (len(inputs) - missing_nr_of_batteries + 1)])
    next_biggest_int_idx = inputs.index(next_biggest_int)
    return __max_joltage_of_battery_bank_recursive(
        inputs[(next_biggest_int_idx + 1) :],
        current_build + [next_biggest_int],
        missing_nr_of_batteries - 1,
    )


def sum_max_joltages(input: list[str], nr_of_required_battiers) -> int:
    return sum([max_joltage_of_battery_bank(i, nr_of_required_battiers) for i in input])


def solution_a():
    with open("src/year_2025/day_03.txt") as f:
        lines = [line.rstrip() for line in f]
        return sum_max_joltages(lines, 2)


def solution_b():
    with open("src/year_2025/day_03.txt") as f:
        lines = [line.rstrip() for line in f]
        return sum_max_joltages(lines, 12)
