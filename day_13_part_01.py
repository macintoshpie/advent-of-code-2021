from python_utils import readlines


EMPTY = '.'
MARKED = '#'


def parse_input(lines):
    dots = []
    
    line_idx = 0
    while True:
        if not lines[line_idx]:
            break

        x, y = [int(v) for v in lines[line_idx].split(',')]
        dots.append((x, y))
        line_idx += 1

    fold_lines = []
    for line in lines[line_idx + 1:]:
        instruction, amount = line.split('=')
        direction = 'x' if 'x' in instruction else 'y'
        amount = int(amount)
        fold_lines.append((direction, amount))
    
    return dots, fold_lines


def print_dots(dots):
    width = max([d[0] for d in dots]) + 1
    height = max([d[1] for d in dots]) + 1
    grid = []
    for _ in range(height):
        grid.append([EMPTY] * width)

    for dot in dots:
        grid[dot[1]][dot[0]] = MARKED

    for row in grid:
        print(''.join(row))

def main():
    input = [l.strip() for l in readlines()]

    dots, folds = parse_input(input)
    dots = set(dots)
    folds = [folds[0]]
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

    print(len(dots))


if __name__ == '__main__':
    main()
