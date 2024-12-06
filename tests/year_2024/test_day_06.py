from src.year_2024.day_06 import (
    distinct_guard_positions,
    solution_a,
    number_of_obstacles_to_create_loop,
    solution_b,
)


def test_distinct_guard_positions():
    test_input = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]

    assert len(distinct_guard_positions(test_input)) == 41


def test_number_of_obstacles_to_create_loop():
    test_input = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]

    assert number_of_obstacles_to_create_loop(test_input) == 6


def test_solution_a():
    assert solution_a() == 4883


def test_solution_b():
    assert solution_b() == 1655
