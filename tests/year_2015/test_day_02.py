from src.year_2015.day_02 import wrapping_paper, solution_a, ribbon, solution_b


def test_wrapping_paper():
    assert wrapping_paper("2x3x4") == 58
    assert wrapping_paper("1x1x10") == 43


def test_ribbon():
    assert ribbon("2x3x4") == 34
    assert ribbon("1x1x10") == 14


def test_solution_a():
    assert solution_a() == 1598415


def test_solution_b():
    assert solution_b() == 3812909
