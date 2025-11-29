from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 31

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert _score(input_test) == expected

def _score(s: str) -> int:
    left = []
    right = []
    
    for line in s.splitlines():
        id1, id2 = line.split()
        left.append(int(id1))
        right.append(int(id2))
    
    score = (right.count(id)*id for id in left)
    
    return sum(score)


def main():
    with open(INPUT_TXT) as f:
       print(_score(f.read()))

if __name__ == "__main__":
    main()