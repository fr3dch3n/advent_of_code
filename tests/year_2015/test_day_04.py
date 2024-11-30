from src.year_2015.day_04 import find_leading_zeroes, solution_a, solution_b


def test_find_leading_zeroes():
    assert find_leading_zeroes("abcdef", "00000") == 609043
    assert find_leading_zeroes("pqrstuv", "00000") == 1048970


def test_solution_a():
    assert solution_a() == 117946


def test_solution_b():
    assert solution_b() == 3938038
