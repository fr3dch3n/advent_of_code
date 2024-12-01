from src.year_2022.day_01 import (
    find_elf_most_calories,
    solution_a,
    find_top_three_elves_most_calories,
    solution_b,
)


def test_find_elf_most_calories():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    assert find_elf_most_calories(input) == 24000


def test_find_top_three_elves_most_calories():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    assert find_top_three_elves_most_calories(input) == 45000


def test_solution_a():
    assert solution_a() == 74711


def test_solution_b():
    assert solution_b() == 209481
