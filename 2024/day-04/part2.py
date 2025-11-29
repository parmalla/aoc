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
EXPECTED = 9

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
    
    def _has_mas(x: int, y: int) -> bool:
        m_pos = []
        s_pos = []
        for direction in _directions():
            xx = x + direction[0]
            yy = y + direction[1]
            if not ((0 <= xx < m) and (0 <= yy < n)):
                return False
            char = lines[xx][yy]
            match char:
                case "M":
                    m_pos.append((xx, yy))
                    if len(m_pos) > 2:
                        return False
                case "S":
                    s_pos.append((xx, yy))
                    if len(s_pos) > 2:
                        return False
                case _:
                    return False
                
        if (m_pos[0][0] - m_pos[1][0] != 0 and m_pos[0][1] - m_pos[1][1] != 0):
            return False
        
        return True
    
    for x in range(m):
        for y in range(n):
            if lines[x][y] == "A":
                result += _has_mas(x, y)
                    
    return result

def _directions() -> Generator[tuple[int, int]]:
    for _n_y in (-1, 1):
        for _n_x in (-1, 1):
            yield (_n_x, _n_y) 


def main():
    with open(INPUT_TXT) as f:
       print(_count(f.read()))

if __name__ == "__main__":
    main()