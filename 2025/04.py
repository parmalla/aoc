"""🎄 Solution for Day 4 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 04.py
"""

from collections.abc import Generator

inp = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
part1_asserts = [
    (inp, 13),
]
part2_asserts = [
    (inp, 43),
]


def directions() -> Generator[tuple[int, int]]:
    for y in (-1, 0, 1):
        for x in (-1, 0, 1):
            if x == y == 0:
                continue
            yield (x, y)


def n_rolls(lines: list[str], remove: bool = False) -> int:
    count = 0
    m = len(lines)
    n = len(lines[0])

    def _accessible(x, y) -> bool:
        adj_count = 0
        for direction in directions():
            xx = x + direction[0]
            yy = y + direction[1]
            if (0 <= xx < m) and (0 <= yy < n):
                adj_count += lines[xx][yy] == "@"

        return adj_count < 4

    for x in range(m):
        for y in range(n):
            if lines[x][y] == "@":
                if _accessible(x, y):
                    count += 1
                    if remove:
                        lines[x] = lines[x][:y] + "." + lines[x][y + 1:]

    return lines, count


def parse_input(inp: str) -> list[str]:
    return inp.splitlines()


def part1(inp: str) -> str | int | None:
    inp = parse_input(inp)
    _, count = n_rolls(inp)
    return count


def part2(inp: str) -> str | int | None:
    inp = parse_input(inp)
    count = 0
    state_count = 1

    while state_count:
        inp, state_count = n_rolls(inp, remove=True)
        count += state_count

    return count


def main():
    part2(inp)

if __name__ == "__main__":
    main()
