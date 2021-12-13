from python_utils import readlines
from day_13_part_01 import (
    print_dots,
    parse_input
)

def main():
    input = [l.strip() for l in readlines()]

    dots, folds = parse_input(input)
    dots = set(dots)
    for fold in folds:
        fold_dir, fold_line = fold
        new_dots = set()
        for dot in dots:
            new_x, new_y = dot
            if fold_dir == 'y' and dot[1] > fold_line:
                new_y = fold_line - (new_y - fold_line)
            if fold_dir == 'x' and dot[0] > fold_line:
                new_x = fold_line - (new_x - fold_line)
            
            new_dots.add((new_x, new_y))

        dots = new_dots

    print_dots(dots)


if __name__ == '__main__':
    main()
