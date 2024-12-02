from src.year_2015.day_05 import is_nice, solution_a, is_nice_v2, solution_b


def test_is_nice():
    assert is_nice("ugknbfddgicrmopn") == True
    assert is_nice("aaa") == True
    assert is_nice("jchzalrnumimnmhp") == False
    assert is_nice("haegwjzuvuyypxyu") == False
    assert is_nice("dvszwmarrgswjxmb") == False


def test_is_nice_v2():
    assert is_nice_v2("qjhvhtzxzqqjkmpb") == True
    assert is_nice_v2("xxyxx") == True
    assert is_nice_v2("uurcxstgmygtbstg") == False
    assert is_nice_v2("ieodomkazucvgmuy") == False


def test_solution_a():
    assert solution_a() == 238


def test_solution_b():
    assert solution_b() == 69
