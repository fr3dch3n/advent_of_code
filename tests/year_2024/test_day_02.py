from src.year_2024.day_02 import (
    is_report_safe,
    solution_a,
    problem_dampener,
    solution_b,
)


def test_is_report_safe():
    assert is_report_safe([7, 6, 4, 2, 1]) == True
    assert is_report_safe([1, 2, 7, 8, 9]) == False
    assert is_report_safe([9, 7, 6, 2, 1]) == False
    assert is_report_safe([1, 3, 2, 4, 5]) == False
    assert is_report_safe([8, 6, 4, 4, 1]) == False
    assert is_report_safe([1, 3, 6, 7, 9]) == True


def test_problem_dampener():
    assert problem_dampener([7, 6, 4, 2, 1]) == True
    assert problem_dampener([1, 2, 7, 8, 9]) == False
    assert problem_dampener([9, 7, 6, 2, 1]) == False
    assert problem_dampener([1, 3, 2, 4, 5]) == True
    assert problem_dampener([8, 6, 4, 4, 1]) == True
    assert problem_dampener([1, 3, 6, 7, 9]) == True


def test_solution_a():
    assert solution_a() == 359


def test_solution_b():
    assert solution_b() == 418
