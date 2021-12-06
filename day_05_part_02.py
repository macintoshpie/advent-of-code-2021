from typing import DefaultDict, NamedTuple

from python_utils import readlines
from day_05_part_01 import (
    parse_line,
    line_to_points,
    Point,
)


def main():
    input = [l.strip() for l in readlines()]
    lines = [parse_line(input_line) for input_line in input]

    num_overlaps = 0
    all_points_covered: dict[Point, int] = DefaultDict(lambda: 0)
    for line in lines:
        for point in line_to_points(line):
            all_points_covered[point] += 1

            if all_points_covered[point] == 2:
                num_overlaps += 1

    print(num_overlaps)


if __name__ == '__main__':
    main()
