from src.year_2025.day_03 import (
    max_joltage_of_battery_bank,
    solution_a,
    solution_b,
    sum_max_joltages,
)


def test_max_joltage_of_battery_bank():
    assert max_joltage_of_battery_bank("987654321111111", 2) == 98
    assert max_joltage_of_battery_bank("811111111111119", 2) == 89
    assert max_joltage_of_battery_bank("234234234234278", 2) == 78
    assert max_joltage_of_battery_bank("818181911112111", 2) == 92
    assert max_joltage_of_battery_bank("987654321111111", 12) == 987654321111
    assert max_joltage_of_battery_bank("811111111111119", 12) == 811111111119
    assert max_joltage_of_battery_bank("234234234234278", 12) == 434234234278
    assert max_joltage_of_battery_bank("818181911112111", 12) == 888911112111


def test_sum_max_joltages():
    input = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    assert sum_max_joltages(input, 2) == 357


def test_solution_a():
    assert solution_a() == 17278


def test_solution_b():
    assert solution_b() == 171528556468625
