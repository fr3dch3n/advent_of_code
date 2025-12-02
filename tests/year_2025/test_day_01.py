from src.year_2025.day_01 import (
    dial,
    how_often_ends_at_zero,
    how_often_passed_zero,
    solution_a,
    solution_b,
)


def test_dial():
    assert dial(0, "R1") == (1, 0)
    assert dial(50, "L68") == (82, 1)


def test_how_often_ends_at_zero():
    instructions = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert how_often_ends_at_zero(instructions) == 3


def test_how_often_passed_zero():
    instructions = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert how_often_passed_zero(instructions) == 6


def test_solution_a():
    assert solution_a() == 1007


def test_solution_b():
    assert solution_b() == 5820
