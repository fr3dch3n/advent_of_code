from src.year_2025.day_06 import (
    grand_total,
    map_to_from_right,
    parse_input,
    solution_a,
    solution_b,
)


def test_parse_input():
    input = ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  "]
    expected = [
        ["123", " 45", "  6", "*  "],
        ["328", "64 ", "98 ", "+  "],
        [" 51", "387", "215", "*  "],
        ["64 ", "23 ", "314", "+  "],
    ]
    assert parse_input(input) == expected


def test_grand_total():
    input = [
        ["123", " 45", "  6", "*  "],
        ["328", "64 ", "98 ", "+  "],
        [" 51", "387", "215", "*  "],
        ["64 ", "23 ", "314", "+  "],
    ]
    assert grand_total(input) == 4277556


def test_map_to_from_right():
    input = [
        ["123", " 45", "  6", "*  "],
        ["328", "64 ", "98 ", "+  "],
        [" 51", "387", "215", "*  "],
        ["64 ", "23 ", "314", "+  "],
    ]
    expected = [
        ["356", "24", "1", "*"],
        ["8", "248", "369", "+"],
        ["175", "581", "32", "*"],
        ["4", "431", "623", "+"],
    ]
    assert map_to_from_right(input) == expected


def test_grand_total_with_map_to_from_right():
    input = [
        ["123", " 45", "  6", "*  "],
        ["328", "64 ", "98 ", "+  "],
        [" 51", "387", "215", "*  "],
        ["64 ", "23 ", "314", "+  "],
    ]
    assert grand_total(input, map_to_from_right) == 3263827


def test_solution_a():
    assert solution_a() == 8108520669952


def test_solution_b():
    assert solution_b() == 11708563470209
