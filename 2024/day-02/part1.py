from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert _safe(input_test) == expected
    
def _report_safety(report: list[int]) -> bool:
    is_increasing = 1
    
    if report[0] < report[1]:
        is_increasing = 1
    elif report[0] > report[1]:
        is_increasing = -1
    else:
        return False
    
    pointer = 0
    while pointer < len(report)-1:
        diff = abs(report[pointer]-report[pointer+1])
        if (report[pointer]*is_increasing < report[pointer+1]*is_increasing
            and (0 < diff < 4)
            ):
            pointer = pointer + 1
        else:
            return False
    
    return True

def _safe(s: str) -> int:
    safe = []
    
    for line in s.splitlines():
        report = line.split()
        report = [int(level) for level in report]
        safe.append(_report_safety(report))

    return sum(safe)


def main():
    with open(INPUT_TXT) as f:
       print(_safe(f.read()))

if __name__ == "__main__":
    main()