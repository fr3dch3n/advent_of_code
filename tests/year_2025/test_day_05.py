from src.year_2025.day_05 import (
    how_many_fresh_ingredients,
    how_many_ingredients_are_spoiled,
    solution_a,
    solution_b,
)


def test_how_many_ingredients_are_spoiled():
    ingredients = [1, 5, 8, 11, 17, 32]
    ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]

    assert how_many_ingredients_are_spoiled(ingredients, ranges) == 3


def test_how_many_fresh_ingredients():
    ranges = [[3, 5], [10, 14], [16, 20], [12, 18]]

    assert how_many_fresh_ingredients(ranges) == 14


def test_solution_a():
    assert solution_a() == 577


def test_solution_b():
    assert solution_b() == 350513176552950
