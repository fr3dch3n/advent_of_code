from src.year_2022.day_02 import (
    total_score,
    solution_a,
    fight,
    strategy_fight,
    solution_b,
)


def test_total_score_fight():
    input = [
        "A Y",
        "B X",
        "C Z",
    ]
    assert total_score(input, fight) == 15


def test_total_score_strategy_fight():
    input = [
        "A Y",
        "B X",
        "C Z",
    ]
    assert total_score(input, strategy_fight) == 12


def test_solution_a():
    assert solution_a() == 12156


def test_solution_b():
    assert solution_b() == 10835
