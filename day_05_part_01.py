from typing import DefaultDict, Generator, NamedTuple

from python_utils import readlines


Point = NamedTuple("Point", [('x', int), ('y', int)])
Line = NamedTuple("Line", [('a', Point), ('b', Point)])


def parse_line(line: str) -> Line:
    point_a_raw, point_b_raw = line.split(' -> ')
    point_a_x, point_a_y = [int(v) for v in point_a_raw.split(',')]
    point_b_x, point_b_y = [int(v) for v in point_b_raw.split(',')]
    return Line(
        Point(point_a_x, point_a_y),
        Point(point_b_x, point_b_y)
    )


def line_to_points(line: Line) -> Generator[Point, None, None]:
    start_point, end_point = sorted([line.a, line.b], key=lambda point: (point.x, point.y))
    x_step = 0 if start_point.x == end_point.x else 1
    y_step = bool(start_point.y != end_point.y) * (1 if end_point.y - start_point.y > 0 else -1)

    for i in range(max(end_point.x - start_point.x, end_point.y - start_point.y) + 1):
        yield Point(
            start_point.x + (i * x_step),
            start_point.y + (i * y_step)
        )


def main():
    input = [l.strip() for l in readlines()]
    lines = [parse_line(input_line) for input_line in input]

    # only consider horizontal and vertical lines
    lines = [
        line
        for line in lines
        if line.a.x == line.b.x or line.a.y == line.b.y
    ]

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
