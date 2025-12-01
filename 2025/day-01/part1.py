from itertools import accumulate
from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
'''
EXPECTED = 3

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert password(input_test) == expected

def password(s: str) -> int:
    rotations = [(line[0], int(line[1:])) for line in s.splitlines()]
    pointer = 50
    rotations = [(-1 if direction == "L" else 1) * steps for direction, steps in rotations]
    
    positions = accumulate(
        rotations, 
        lambda _pointer, _step: (_pointer + _step) % 100, 
        initial=pointer
    )
    
    return sum(position == 0 for position in positions)


def main():
    with open(INPUT_TXT) as f:
       print(password(f.read()))

if __name__ == "__main__":
    main()