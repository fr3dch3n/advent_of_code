from src.year_2024.day_01 import (
    find_lists_distance,
    solution_a,
    find_similarity_distance,
    solution_b,
)


def test_find_lists_distance():
    input = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    assert find_lists_distance(input) == 11


def test_find_similarity_distance():
    input = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    assert find_similarity_distance(input) == 31


def test_solution_a():
    assert solution_a() == 1722302


def test_solution_b():
    assert solution_b() == 20373490
