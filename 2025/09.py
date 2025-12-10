"""🎄 Solution for Day 9 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 09.py
"""

from itertools import combinations

inp = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
part1_asserts = [
    (inp, 50),
]
part2_asserts = [
    (inp, 24),
]


def parse_input(inp: str):
    points = [
        tuple(map(int, line.split(",")))
        for line in inp.splitlines()
    ]

    return points


def part1(inp: str) -> str | int | None:
    points = parse_input(inp)
    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(points, 2)
    )


def boundary(diag_point1, diag_point2, points):
    pass

def part2(inp: str) -> str | int | None:
    points = parse_input(inp)
    return max(
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        for (x1, y1), (x2, y2) in combinations(points, 2)
        if boundary((x1, y1), (x2, y2), points)
    )


def main():
    print(part2(inp))


if __name__ == "__main__":
    main()
