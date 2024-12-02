import functools

from src.utils import read_input

data = {}


def build_data_dict(lines: list[str]):
    for line in lines:
        cmd, key = line.split(" -> ")
        data[key.strip()] = cmd


@functools.lru_cache()
def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    cmd = data[key].split(" ")

    if "NOT" in cmd:
        return ~get_value(cmd[1])
    if "AND" in cmd:
        return get_value(cmd[0]) & get_value(cmd[2])
    elif "OR" in cmd:
        return get_value(cmd[0]) | get_value(cmd[2])
    elif "LSHIFT" in cmd:
        return get_value(cmd[0]) << get_value(cmd[2])
    elif "RSHIFT" in cmd:
        return get_value(cmd[0]) >> get_value(cmd[2])
    else:
        return get_value(cmd[0])


def solution_a() -> int:
    lines = read_input(2015, 7)
    build_data_dict(lines)
    return get_value("a")


def solution_b() -> int:
    lines = read_input(2015, 7)
    build_data_dict(lines)
    data["b"] = str(get_value("a"))
    get_value.cache_clear()
    return get_value("a")
