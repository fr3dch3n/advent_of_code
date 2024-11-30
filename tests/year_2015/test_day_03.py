from src.year_2015.day_03 import house_with_at_least_one_present, solution_a, solution_b


def test_house_with_at_least_one_present():
    assert len(set(house_with_at_least_one_present(">"))) == 2
    assert len(set(house_with_at_least_one_present("^>v<"))) == 4
    assert len(set(house_with_at_least_one_present("^v^v^v^v^v"))) == 2


def test_solution_a():
    assert solution_a() == 2572


def test_solution_b():
    assert solution_b() == 2631
