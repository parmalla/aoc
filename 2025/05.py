"""🎄 Solution for Day 5 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 05.py
"""

inp = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
part1_asserts = [
    (inp, 3),
]
part2_asserts = [
    (inp, 14),
]


def parse_input(inp: str) -> tuple[tuple[int, int], list[int]]:
    lines = inp.splitlines()
    blank_idx = 0
    for i, line in enumerate(lines):
        if line == "":
            blank_idx = i
            break

    fresh_ranges = [
        tuple(map(int, line.split("-")))
        for line in lines[:blank_idx]
    ]
    ingredients = list(map(int, lines[blank_idx + 1:]))

    return fresh_ranges, ingredients


def normalized_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges = sorted(ranges, key=lambda r: r[0])

    normalized_ranges = []
    for start, end in ranges:
        if not normalized_ranges or start > normalized_ranges[-1][1] + 1:
            normalized_ranges.append([start, end])
        else:
            normalized_ranges[-1][1] = max(normalized_ranges[-1][1], end)

    return list(map(tuple, normalized_ranges))


def n_fresh(fresh_ranges, ingredients):
    normalized_fresh = normalized_ranges(fresh_ranges)

    count = 0
    for ingredient in ingredients:
        for start, end in normalized_fresh:
            if ingredient < start:
                break
            elif start <= ingredient <= end:
                count += 1

    return count


def part1(inp: str) -> str | int | None:
    fresh_ranges, ingredients = parse_input(inp)
    return n_fresh(fresh_ranges, ingredients)


def part2(inp: str) -> str | int | None:
    fresh_ranges, _ = parse_input(inp)
    fresh_ranges = normalized_ranges(fresh_ranges)
    return sum(end - start + 1 for start, end in fresh_ranges)


def main():
    part2(inp)


if __name__ == "__main__":
    main()
