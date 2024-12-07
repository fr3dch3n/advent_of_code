from src.year_2024.day_07 import (
    is_possible_equation,
    solution_a,
    sum_possible_equations,
    solution_b,
)


def test_is_possible_equation():
    assert is_possible_equation("190: 10 19", ["+", "*"]) == True
    assert is_possible_equation("3267: 81 40 27", ["+", "*"]) == True
    assert is_possible_equation("292: 11 6 16 20", ["+", "*"]) == True

    assert is_possible_equation("156: 15 6", ["+", "*", "||"]) == True
    assert is_possible_equation("7290: 6 8 6 15", ["+", "*", "||"]) == True
    assert is_possible_equation("192: 17 8 14", ["+", "*", "||"]) == True


def test_sum_possible_equations():
    assert (
        sum_possible_equations(
            [
                "190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20",
            ],
            ["+", "*"],
        )
        == 3749
    )

    assert (
        sum_possible_equations(
            [
                "190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20",
            ],
            ["+", "*", "||"],
        )
        == 11387
    )


def test_solution_a():
    assert solution_a() == 1611660863222


def test_solution_b():
    assert solution_b() == 945341732469724
