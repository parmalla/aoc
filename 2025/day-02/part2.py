import math
import re
from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
'''
EXPECTED = 4174379265 

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert sum_invalid(input_test) == expected
    
def invalid(n: int) -> bool:
    digits = math.floor(math.log10(n)) + 1
    
    half = digits // 2
    str_n = str(n)
    for i in range(1, half + 1):
        if digits % i == 0:
            pattern = str_n[:i]
            re_pattern = re.compile(f"({pattern}){{{digits // i}}}")
            if re.fullmatch(re_pattern, str_n):
                return True

    return False

def sum_invalid(s: str) -> int:
    ranges = [
        tuple(map(int, part.split("-")))
        for part in s.strip().split(",")
    ]
    
    invalid_sum = 0
    for start, end in ranges:
        invalid_sum += sum(
            n for n in range(start, end + 1)
            if invalid(n)
        )
        
    return invalid_sum


def main():
    with open(INPUT_TXT) as f:
       print(sum_invalid(f.read()))

if __name__ == "__main__":
    main()