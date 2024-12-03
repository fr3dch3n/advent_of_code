from src.year_2024.day_03 import (
    sum_all_muls,
    solution_a,
    sum_all_enabled_muls,
    solution_b,
)


def test_sum_all_muls():
    assert (
        sum_all_muls(
            ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
        )
        == 161
    )


def test_sum_all_enabled_muls():
    assert (
        sum_all_enabled_muls(
            [
                "do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
            ]
        )
        == 48
    )


def test_solution_a():
    assert solution_a() == 179834255


def test_solution_b():
    assert solution_b() == 80570939
