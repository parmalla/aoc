"""🎄 Solution for Day 10 of Advent of Code 2025 🎄

Usage:

uv run adventofcode run 10.py
"""
from collections import deque

inp = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
part1_asserts = [
    (inp, 7),
]
part2_asserts = [
    (inp, None),
]


def parse_input(inp: str):
    result = []
    for line in inp.splitlines():
        lights, *schematics, joltages = line.split()
        lights = {i for i, state in enumerate(lights[1:-1]) if state == "#"}
        schematics = [
            set(map(int, schematic[1:-1].split(",")))
            for schematic in schematics
        ]
        joltages = list(map(int, joltages[1:-1].split(",")))
        result.append((lights, schematics, joltages))

    return result


def min_schematics(lights, schematics):
    states = deque([(frozenset(), 0)])
    visited = {frozenset()}

    while states:
        state, count = states.popleft()

        if state == lights:
            return count

        for schematic in schematics:
            curr_state = state ^ schematic

            if curr_state not in visited:
                states.append((curr_state, count + 1))
                visited.add(curr_state)


def part1(inp: str) -> str | int | None:
    machines_state = parse_input(inp)
    return sum(
        min_schematics(lights, schematics)
        for (lights, schematics, _) in machines_state
    )


def part2(inp: str) -> str | int | None:
    return None


def main():
    print(part1(inp))


if __name__ == "__main__":
    main()
