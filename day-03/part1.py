import re
from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"

INPUT_TEST = '''\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''
EXPECTED = 48

@pytest.mark.parametrize(
    ("input_test", "expected"),
    (
        (INPUT_TEST, EXPECTED),
    )
)
def test(input_test: str, expected: int) -> None:
    assert _mull(input_test) == expected
    
def _read_memory(corrupt_memory: str) -> int:
    mul_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = mul_regex.findall(corrupt_memory)
    result = (int(x)*int(y) for x, y in result)
    
    return sum(result)

def _mull(s: str) -> int:
    output = []
    
    for line in s.splitlines():
        output.append(_read_memory(line))

    return sum(output)


def main():
    with open(INPUT_TXT) as f:
       print(_mull(f.read()))

if __name__ == "__main__":
    main()