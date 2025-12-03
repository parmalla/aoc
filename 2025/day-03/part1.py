from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
987654321111111
811111111111119
234234234234278
818181911112111
'''
EXPECTED = 357

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert joltage(input_test) == expected


def max_joltage_bank(bank: str) -> int:
    bank_jolts = set(bank)
    bank_jolts = list(sorted(map(int, bank_jolts)))
    jolt_positions = {bank_jolt: [] for bank_jolt in bank_jolts}
    for i, bank_jolt in enumerate(bank):
        jolt_positions[int(bank_jolt)].append(i)
    for k in jolt_positions.keys():
        jolt_positions[k].sort()

    while bank_jolts:
        bank_jolt = bank_jolts.pop()
        positions = jolt_positions[bank_jolt]

        pos = positions[0]
        for other_jolt in range(9, -1, -1):
            other_positions = jolt_positions.get(other_jolt, [])
            if other_jolt == bank_jolt and len(positions) > 1:
                return bank_jolt * 10 + other_jolt
            if not other_positions:
                continue
            if pos < other_positions[-1]:
                return bank_jolt * 10 + other_jolt


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