from src.utils import read_input


def total_score(input: list[str], fight_fn) -> int:
    score = 0
    for i in input:
        op = i.split()[0]
        me = i.split()[1]
        score += fight_fn(op, me)
    return score


def fight(op: str, me: str) -> int:
    op_score = to_score(op)
    me_score = to_score(me)

    if op_score == me_score:
        return me_score + 3
    elif op_score == 1 and me_score == 3:
        return me_score + 0
    elif me_score > op_score or (op_score == 3 and me_score == 1):
        return me_score + 6
    else:
        return me_score + 0


def strategy_fight(op: str, target: str) -> int:
    op_score = to_score(op)

    if target == "Y":  # tie
        return op_score + 3
    elif target == "X":  # loose
        if op_score == 1:
            return 3
        else:
            return op_score - 1
    elif target == "Z":  # win
        if op_score == 3:
            return 1 + 6
        else:
            return op_score + 1 + 6


def to_score(s: str) -> int:
    if s == "A" or s == "X":
        return 1  # Rock
    elif s == "B" or s == "Y":
        return 2  # Paper
    else:
        return 3  # Scissor


def solution_a():
    lines = read_input(2022, 2)
    return total_score(lines, fight)


def solution_b():
    lines = read_input(2022, 2)
    return total_score(lines, strategy_fight)
