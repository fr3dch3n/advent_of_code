from src.year_2024.day_04 import count_xmas, solution_a, count_mas, solution_b


def test_count_xmas():
    assert count_xmas(["XMAS"]) == 1
    assert count_xmas(["XMAS", "M...", "A...", "S..."]) == 2
    assert count_xmas(["XMAS", "M...", "A...", "S...", "...M"]) == 2
    assert count_xmas(["XMAS", ".M..", "..A.", "...S"]) == 2
    assert count_xmas(["SAMX"]) == 1
    assert (
        count_xmas(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 18
    )


def test_count_mas():
    assert count_mas(["M.M", ".A.", "S.S"]) == 1
    assert count_mas(["S.S", ".A.", "M.M"]) == 1
    assert (
        count_mas(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 9
    )


def test_solution_a():
    assert solution_a() == 2504


def test_solution_b():
    assert solution_b() == 1923
