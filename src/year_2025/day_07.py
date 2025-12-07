from collections import defaultdict


def start_position(line: str) -> int:
    return line.index("S")


def line_only_dots(line) -> bool:
    return line == len(line) * line[0]


def find_all(s, c):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)


def replace_at(s, c, i):
    return s[:i] + c + s[(i + 1) :]


def count_splits(lines: list[str]) -> int:
    start = start_position(lines[0])
    splits = 0
    concurrent_beam_pos = set()
    for line in lines[1:]:
        for dp in list(find_all(line, "^")):
            if dp != start and dp not in concurrent_beam_pos:
                continue
            if dp in concurrent_beam_pos:
                concurrent_beam_pos.remove(dp)
            concurrent_beam_pos.add(dp - 1)
            concurrent_beam_pos.add(dp + 1)
            splits += 1
    return splits


def count_timelines(lines: list[str]) -> int:
    start = start_position(lines[0])
    return follow_timeline(lines, start)


def follow_timeline(lines, start):
    beams = defaultdict(int)
    beams[start] = 1

    for line in lines[1:]:
        beams_new = defaultdict(int)
        for c in beams:
            if line[c] == "^":
                beams_new[c - 1] += beams[c]
                beams_new[c + 1] += beams[c]
            else:
                beams_new[c] += beams[c]
        beams = beams_new

    return sum([count for _, count in beams.items()])


def solution_a():
    with open("src/year_2025/day_07.txt") as f:
        lines = [s for s in f.readlines()]
        return count_splits(lines)


def solution_b():
    with open("src/year_2025/day_07.txt") as f:
        lines = [s for s in f.readlines()]
        return count_timelines(lines)
