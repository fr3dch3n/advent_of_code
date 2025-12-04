from src.year_2025.day_04 import (
    how_many_rolls_in_total_can_be_accessed,
    solution_a,
    solution_b,
    which_rolls_can_be_accessed,
)


def test_which_rolls_can_be_accessed():
    input = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    input = [list(s) for s in input]

    assert len(which_rolls_can_be_accessed(input)) == 13


def test_how_many_rolls_in_total_can_be_accessed():
    input = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    input = [list(s) for s in input]

    assert how_many_rolls_in_total_can_be_accessed(input) == 43


def test_solution_a():
    assert solution_a() == 1502


def test_solution_b():
    assert solution_b() == 9083
