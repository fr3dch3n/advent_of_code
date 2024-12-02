def read_input(year: int, day: int) -> list[str]:
    filename = f"inputs/year_{year}/day_{day:02}.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines


def read_raw_input(year: int, day: int) -> list[str]:
    filename = f"inputs/year_{year}/day_{day:02}.txt"
    with open(filename, "r") as file:
        lines = file.read()
        return lines.rstrip().split()
