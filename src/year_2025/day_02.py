def sum_of_invalid_ids_in_range(left, right, validity_check) -> int:
    s = 0
    for n in range(left, right + 1):
        if not validity_check(n):
            s += n

    return s


def sum_of_invalid_ids(raw_ranges: str, validity_check):
    ranges = raw_ranges.split(",")
    s = 0
    for r in ranges:
        ps = r.split("-")
        left = int(ps[0])
        right = int(ps[1])
        s += sum_of_invalid_ids_in_range(left, right, validity_check)
    return s


def id_is_same_twice(id):
    sid = str(id)
    center = int(len(sid) / 2)
    left = sid[center:]
    right = sid[:center]
    return left != right


def id_is_same_multiple_times(id):
    sid = str(id)
    center = int(len(sid) / 2)
    for x in range(0, center + 1):
        subset = sid[0:x]
        if subset == "":
            continue
        subset_length = len(subset)
        nr_of_subsets = int(len(sid) / subset_length)

        if len(sid) % subset_length == 0:
            all_subsets_equal = True
            for n in range(nr_of_subsets):
                subset_to_compare = sid[0 + subset_length * n : x + subset_length * n]
                if subset_to_compare != subset:
                    all_subsets_equal = False
            if all_subsets_equal:
                return False
    return True


def solution_a():
    with open("src/year_2025/day_02.txt") as f:
        lines = [line.rstrip() for line in f]
        return sum_of_invalid_ids(lines[0], id_is_same_twice)


def solution_b():
    with open("src/year_2025/day_02.txt") as f:
        lines = [line.rstrip() for line in f]
        return sum_of_invalid_ids(lines[0], id_is_same_multiple_times)
