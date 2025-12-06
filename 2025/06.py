"""🎄 Solution for Day 6 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 06.py
"""
import operator
import re
from functools import reduce
from itertools import zip_longest

import numpy as np

inp = """\
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
part1_asserts = [
    (inp, 4277556),
]
part2_asserts = [
    (inp, 3263827),
]


def parse_input(inp: str):
    lines = inp.splitlines()
    mat = [
        list(map(int, line.split()))
        for line in lines[:-1]
    ]
    operators = [
        (operator.add, 0) if op == "+" else (operator.mul, 1)
        for op in lines[-1].split()
    ]

    return mat, operators


def parse_alignment(inp: str):
    lines = inp.splitlines()

    re_numbers = re.compile(r"\d+")
    line_matches = [list(re.finditer(re_numbers, line)) for line in lines[:-1]]

    n_cols = len(line_matches[0])
    col_starts = [[] for _ in range(n_cols)]

    for matches in line_matches:
        for i, m in enumerate(matches):
            col_starts[i].append(m.start())

    return [
        "l" if all(s == starts[0] for s in starts) else "r"
        for starts in col_starts
    ]


def get_digits(n: int) -> list[int]:
    return [int(ch) for ch in str(n)]


def digits_to_int(digits: list[int]) -> int:
    n = 0
    for d in digits:
        n = n * 10 + d
    return n


def get_ceph_row(row: list[list[int]], alignment: str) -> list[int]:
    cols = list(zip_longest(*row, fillvalue=None))

    if alignment == "r":
        max_len = len(cols[0])
        padded = [
            tuple([None] * (max_len - len(r)) + r)
            for r in row
        ]
        cols = list(zip_longest(*padded, fillvalue=None))

    nums = []
    for col in cols:
        digits = [d for d in col if d is not None]
        if digits:
            nums.append(digits_to_int(digits))
    return nums[::-1]


def part1(inp: str) -> str | int | None:
    mat, operators = parse_input(inp)
    transposed = np.array(mat).transpose()
    return sum(
        reduce(op, row, initial)
        for row, (op, initial) in zip(transposed, operators)
    )


def part2(inp: str) -> str | int | None:
    mat, operators = parse_input(inp)
    alignments = parse_alignment(inp)
    ceph_mat = [
        get_ceph_row(list(map(get_digits, row)), alignment)
        for row, alignment in zip(np.array(mat).transpose(), alignments)
    ]

    return sum(
        reduce(op, row, initial)
        for row, (op, initial) in zip(ceph_mat, operators)
    )


def main():
    part2(inp)


if __name__ == "__main__":
    main()