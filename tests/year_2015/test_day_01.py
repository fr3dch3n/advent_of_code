from src.year_2015.day_01 import floor_exit, solution_a, entering_basement, solution_b


def test_floor_exit():
    assert floor_exit("(())") == 0
    assert floor_exit(")())())") == -3


def test_entering_basement():
    assert entering_basement(")") == 1
    assert entering_basement("()())") == 5


def test_solution_a():
    assert solution_a() == 280


def test_solution_b():
    assert solution_b() == 1797
