from src.year_2023.day_02 import (
    parse_input,
    game_possible,
    solution_a,
    sum_of_possible_games,
    minimal_set_power,
    solution_b,
)


def test_parse_input():
    assert parse_input(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    ) == (
        3,
        [
            {"green": 8, "blue": 6, "red": 20},
            {"blue": 5, "red": 4, "green": 13},
            {"green": 5, "red": 1},
        ],
    )


def test_game_possible():
    assert (
        game_possible(
            [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ],
            {"red": 12, "green": 13, "blue": 14},
        )
        == False
    )


def test_sum_of_possible_games():
    input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert sum_of_possible_games(input, {"red": 12, "green": 13, "blue": 14}) == 8


def test_minimal_set_power():
    assert (
        minimal_set_power(
            [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ]
        )
        == 1560
    )


def test_solution_a():
    assert solution_a() == 2169


def test_solution_b():
    assert solution_b() == 60948
