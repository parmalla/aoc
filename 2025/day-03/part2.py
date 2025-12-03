from bisect import bisect_right
from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"
REQUIRED_BATTERIES = 12

INPUT_TEST = '''\
987654321111111
811111111111119
234234234234278
818181911112111
'''
EXPECTED = 3121910778619

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert joltage(input_test) == expected


def max_joltage_bank(bank: str) -> int:
    jolt_positions = {int(jolt): [] for jolt in set(bank)}
    for i, jolt in enumerate(bank):
        jolt_positions[int(jolt)].append(i)
    for k in jolt_positions.keys():
        jolt_positions[k].sort()

    total_batteries = len(bank)
    needed = REQUIRED_BATTERIES
    digits = []
    cur_pos = -1

    for i in range(needed):
        rem_needed = needed - i - 1
        for d in range(9, -1, -1):
            positions = jolt_positions.get(d, [])
            idx = bisect_right(positions, cur_pos)
            if idx >= len(positions):
                continue
            p = positions[idx]
            if total_batteries - (p + 1) >= rem_needed:
                digits.append(str(d))
                cur_pos = p
                break

    return int(''.join(digits))


def joltage(s: str) -> int:
    banks = s.splitlines()

    output = sum(
        max_joltage_bank(bank)
        for bank in banks
    )

    return output

def main():
    with open(INPUT_TXT) as f:
       print(joltage(f.read()))

if __name__ == "__main__":
    main()