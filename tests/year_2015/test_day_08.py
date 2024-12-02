from src.year_2015.day_08 import count_string, solution_a, solution_b


def test_count_string():
    assert count_string('""') == 2
    assert count_string('"abc"') == 2
    assert count_string('"aaa\\"aaa"') == 3
    assert count_string('"\\x27"') == 5


def test_solution_a():
    assert solution_a() == 1371


def test_solution_b():
    assert solution_b() == 2117
