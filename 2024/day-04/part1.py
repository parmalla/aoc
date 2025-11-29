from pathlib import Path
from collections.abc import Generator

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
EXPECTED = 18

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert _count(input_test) == expected

def _count(s: str) -> int:
    lines: list[str] = [line for line in s.splitlines()]
    del s
    result = 0
    m = len(lines)
    n = len(lines[0])
    
    def _has_mas(x: int, y: int, direction: tuple[int, int]) -> bool:
        for i, char in enumerate("MAS", start=1):
            xx = x + i * direction[0]
            yy = y + i * direction[1]
            if not ((0 <= xx < m) and (0 <= yy < n)):
                return False
            if lines[xx][yy] != char:
                return False
        return True
    
    for x in range(m):
        for y in range(n):
            if lines[x][y] == "X":
                for direction in _directions():
                    result += _has_mas(x, y, direction)
                    
    return result

def _directions() -> Generator[tuple[int, int]]:
    for _n_y in (-1, 0, 1):
        for _n_x in (-1, 0, 1):
            if _n_y == _n_x == 0:
                continue
            yield (_n_x, _n_y) 


def main():
    with open(INPUT_TXT) as f:
       print(_count(f.read()))

if __name__ == "__main__":
    main()