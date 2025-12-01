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
    count = 0
    
    for rotation in rotations:
        direction, steps = rotation
        if direction == 'L':
            pointer -= steps
        else:
            pointer += steps
        
        pointer %= 100
        if pointer == 0:
            count += 1

    return count 


def main():
    with open(INPUT_TXT) as f:
       print(password(f.read()))

if __name__ == "__main__":
    main()