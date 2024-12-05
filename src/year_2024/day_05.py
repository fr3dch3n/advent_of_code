from src.utils import read_input


def parse_updates(update_lines: list[str]) -> list[list[int]]:
    new_updates = []
    for update in update_lines:
        update_parts = update.split(",")
        new_updates.append([int(u) for u in update_parts])

    return new_updates


def parse_rules(rules_lines: list[str]) -> dict[int, list[int]]:
    rules_dict = {}
    for rule in rules_lines:
        rule_parts = rule.split("|")
        key = int(rule_parts[0])
        value = int(rule_parts[1])
        if key in rules_dict:
            rules_dict[key].append(value)
        else:
            rules_dict[key] = [value]
    return rules_dict


def check_ordering(lines: list[str]) -> int:
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    lines = new_lines

    lines_separate_by_empty_line = lines.index("")
    rules = lines[:lines_separate_by_empty_line]
    updates = lines[lines_separate_by_empty_line + 1 :]
    updates = parse_updates(updates)
    rules = parse_rules(rules)

    incorrect_updates = incorrectly_ordered_updates(rules, updates)

    s = 0
    for update in updates:
        if update not in incorrect_updates:
            s += update[(len(update) // 2)]
    return s


def incorrectly_ordered_updates(rules_dict, updates):
    wrong_ordered = []
    for update in updates:
        all_in_line = True
        for update_val in update:
            if update_val in rules_dict:
                ordering_rule_to_apply = rules_dict[update_val]
                for ordering_rule in ordering_rule_to_apply:
                    if ordering_rule in update:
                        index_of_update_val_in_update = update.index(update_val)
                        index_of_ordering_rule_in_update = update.index(ordering_rule)
                        if (
                            index_of_update_val_in_update
                            > index_of_ordering_rule_in_update
                        ):
                            all_in_line = False
        if not all_in_line:
            wrong_ordered.append(update)
    return wrong_ordered


def check_if_update_is_in_order(update: list[int], rules: dict[int, list[int]]) -> bool:
    for i in range(len(update)):
        if update[i] in rules:
            for rule in rules[update[i]]:
                if rule in update:
                    index_of_rule = update.index(rule)
                    if index_of_rule < i:
                        return False
    return True


def fix_ordering_for_update(
    incorrect_update: list[int], rules: dict[int, list[int]]
) -> list[int]:
    for i in range(len(incorrect_update)):
        if incorrect_update[i] in rules:
            for rule in rules[incorrect_update[i]]:
                if rule in incorrect_update:
                    index_of_rule = incorrect_update.index(rule)
                    if index_of_rule < i:
                        incorrect_update[i], incorrect_update[index_of_rule] = (
                            incorrect_update[index_of_rule],
                            incorrect_update[i],
                        )
                        if not check_if_update_is_in_order(incorrect_update, rules):
                            return fix_ordering_for_update(incorrect_update, rules)

    return incorrect_update


def fix_ordering(lines: list[str]):
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())
    lines = new_lines

    lines_separate_by_empty_line = lines.index("")
    rules = lines[:lines_separate_by_empty_line]
    updates = lines[lines_separate_by_empty_line + 1 :]
    updates = parse_updates(updates)
    rules = parse_rules(rules)

    incorrect_updates = incorrectly_ordered_updates(rules, updates)

    fixed_updates = []
    for incorrect_update in incorrect_updates:
        fixed_updates.append(fix_ordering_for_update(incorrect_update, rules))

    s = 0
    for update in fixed_updates:
        s += update[(len(update) // 2)]
    return s


def solution_a():
    lines = read_input(2024, 5)
    return check_ordering(lines)


def solution_b():
    lines = read_input(2024, 5)
    return fix_ordering(lines)
