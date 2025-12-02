from src.year_2025.day_02 import (
    id_is_same_multiple_times,
    id_is_same_twice,
    solution_a,
    solution_b,
    sum_of_invalid_ids,
)


def test_id_is_same_twice():
    assert id_is_same_twice(12)
    assert id_is_same_twice(1188511886)
    assert not id_is_same_twice(11)
    assert not id_is_same_twice(1188511885)
    assert not id_is_same_twice(222222)
    assert not id_is_same_twice(38593859)
    assert not id_is_same_twice(446446)


def test_id_is_same_multiple_times():
    assert id_is_same_multiple_times(12)
    assert id_is_same_multiple_times(1188511886)
    assert not id_is_same_multiple_times(11)
    assert not id_is_same_multiple_times(1188511885)
    assert not id_is_same_multiple_times(222222)
    assert not id_is_same_multiple_times(38593859)
    assert not id_is_same_multiple_times(446446)
    assert not id_is_same_multiple_times(824824824)
    assert not id_is_same_multiple_times(2121212121)


def test_sum_of_invalid_ids():
    input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,
    446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    assert sum_of_invalid_ids(input, id_is_same_twice) == 1227775554
    assert sum_of_invalid_ids(input, id_is_same_multiple_times) == 4174379265


def test_solution_a():
    assert solution_a() == 19574776074


def test_solution_b():
    assert solution_b() == 25912654282
