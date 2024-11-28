from src.utils import read_input


def wrapping_paper(dims: str) -> int:
    p = [int(x) for x in dims.split("x")]
    wraps = [p[0] * p[1], p[1] * p[2], p[2] * p[0]]
    return sum(2 * wraps, min(wraps))


def ribbon(dims: str) -> int:
    p = sorted([int(x) for x in dims.split("x")])
    return p[0] * 2 + p[1] * 2 + (p[0] * p[1] * p[2])


def solution_a() -> int:
    lines = read_input(2015, 2)
    return sum([wrapping_paper(dims) for dims in lines])


def solution_b() -> int:
    lines = read_input(2015, 2)
    return sum([ribbon(dims) for dims in lines])
