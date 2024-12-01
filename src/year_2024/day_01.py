from collections import Counter

from src.utils import read_input


def find_lists_distance(input: list[str]) -> int:
    lefts, rights = partition(input)
    lefts.sort()
    rights.sort()

    return sum([abs(x - y) for (x, y) in zip(lefts, rights)])


def partition(input: list[str]) -> (list[int], list[int]):
    lefts = []
    rights = []
    for i in input:
        p = i.split()
        lefts.append(int(p[0]))
        rights.append(int(p[1]))
    return lefts, rights


def find_similarity_distance(input: list[str]) -> int:
    lefts, rights = partition(input)
    rights_counts = Counter(rights)
    return sum([l * rights_counts[l] for l in lefts])


def solution_a():
    lines = read_input(2024, 1)
    return find_lists_distance(lines)


def solution_b():
    lines = read_input(2024, 1)
    return find_similarity_distance(lines)
