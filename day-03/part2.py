import re
from pathlib import Path

import pytest

INPUT_TXT = Path(__file__).parent / "input.txt"


INPUT_TEST = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
don't()do()xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
EXPECTED = 322

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
    do_regex = re.compile(r"do\(\)")
    dont_regex = re.compile(r"don\'t\(\)")
    
    mul_pos = [m.start() for m in mul_regex.finditer(corrupt_memory)]
    do_pos = [m.start() for m in do_regex.finditer(corrupt_memory)]
    dont_pos = [m.start() for m in dont_regex.finditer(corrupt_memory)]
    do_operation = []
    instructions = sorted(do_pos + dont_pos)
    
    for pos in mul_pos:
        recent_instruction = max((instr for instr in instructions if instr < pos), default=None)
        if recent_instruction:
            instructions = instructions[instructions.index(recent_instruction):]
    
        if recent_instruction in do_pos:
            do_operation.append(True)
        elif recent_instruction in dont_pos:
            do_operation.append(False)
        else:
            do_operation.append(True)

    result = mul_regex.findall(corrupt_memory)
    result = (int(x)*int(y) for (x, y), do_mul in zip(result, do_operation) if do_mul)
    
    return sum(result)

def _mull(s: str) -> int:
    s = "".join(s.splitlines())
    return _read_memory(s)


def main():
    with open(INPUT_TXT) as f:
       print(_mull(f.read()))

if __name__ == "__main__":
    main()