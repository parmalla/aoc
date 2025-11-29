from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
EXPECTED = 143

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