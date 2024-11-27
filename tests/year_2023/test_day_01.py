from src.year_2023.day_01 import (
    calibration_value,
    solution_a,
    nouns_calibration_value,
    solution_b,
)


def test_calibration_value():
    assert calibration_value("1abc2") == 12
    assert calibration_value("pqr3stu8vwx") == 38
    assert calibration_value("a1b2c3d4e5f") == 15
    assert calibration_value("treb7uchet") == 77


def test_nouns_calibration_value():
    assert nouns_calibration_value("two1nine") == 29
    assert nouns_calibration_value("eightwothree") == 83
    assert nouns_calibration_value("abcone2threexyz") == 13
    assert nouns_calibration_value("xtwone3four") == 24
    assert nouns_calibration_value("4nineeightseven2") == 42
    assert nouns_calibration_value("zoneight234") == 14
    assert nouns_calibration_value("7pqrstsixteen") == 76


def test_solution_a():
    assert solution_a() == 54304


def test_solution_b():
    assert solution_b() == 54418
