from src.year_2024.day_05 import (
    check_ordering,
    solution_a,
    incorrectly_ordered_updates,
    fix_ordering_for_update,
    solution_b,
)


def test_check_ordering():
    test_input = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]

    assert check_ordering(test_input) == 143


def test_incorrectly_ordered_updates():
    rules_dict = {
        47: [53, 13, 61, 29],
        97: [13, 61, 47, 29, 53, 75],
        75: [29, 53, 47, 61, 13],
        61: [13, 53, 29],
        29: [13],
        53: [29, 13],
    }

    assert incorrectly_ordered_updates(rules_dict, [[75, 47, 61, 53, 29]]) == []
    assert incorrectly_ordered_updates(rules_dict, [[97, 61, 53, 29, 13]]) == []
    assert incorrectly_ordered_updates(rules_dict, [[75, 29, 13]]) == []
    assert incorrectly_ordered_updates(rules_dict, [[75, 97, 47, 61, 53]]) == [
        [75, 97, 47, 61, 53]
    ]
    assert incorrectly_ordered_updates(rules_dict, [[61, 13, 29]]) == [[61, 13, 29]]
    assert incorrectly_ordered_updates(rules_dict, [[97, 13, 75, 29, 47]]) == [
        [97, 13, 75, 29, 47]
    ]


def test_fix_ordering_for_update():
    rules_dict = {
        47: [53, 13, 61, 29],
        97: [13, 61, 47, 29, 53, 75],
        75: [29, 53, 47, 61, 13],
        61: [13, 53, 29],
        29: [13],
        53: [29, 13],
    }

    assert fix_ordering_for_update([75, 97, 47, 61, 53], rules_dict) == [
        97,
        75,
        47,
        61,
        53,
    ]
    assert fix_ordering_for_update([61, 13, 29], rules_dict) == [61, 29, 13]
    assert fix_ordering_for_update([97, 13, 75, 29, 47], rules_dict) == [
        97,
        75,
        47,
        29,
        13,
    ]


def test_solution_a():
    assert solution_a() == 5651


def test_solution_b():
    assert solution_b() == 4743
