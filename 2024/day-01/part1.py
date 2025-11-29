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
EXPECTED = 11

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert _distance(input_test) == expected

def _distance(s: str) -> int:
    first = []
    second = []
    
    for line in s.splitlines():
        id1, id2 = line.split()
        first.append(int(id1))
        second.append(int(id2))
    
    first.sort()
    second.sort()
    distance = (abs(fid-sid) for fid, sid in zip(first, second))
    
    return sum(distance)


def main():
    with open(INPUT_TXT) as f:
       print(_distance(f.read()))

if __name__ == "__main__":
    main()