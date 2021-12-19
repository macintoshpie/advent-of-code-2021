from python_utils import readlines


def simulate(x, y, x_min, x_max, y_min, y_max):
    max_y = float('-inf')
    pos_x = 0
    pos_y = 0
    v_x = x
    v_y = y
    while True:
        pos_x = pos_x + v_x
        pos_y = pos_y + v_y
        max_y = max(max_y, pos_y)
        v_x = v_x - 1 if v_x > 0 else 0
        v_y = v_y - 1

        if (
            x_min <= pos_x and pos_x <= x_max
            and y_min <= pos_y and pos_y <= y_max
        ):
            # Hit!
            return True, max_y
        if pos_x > x_max:
            # overshot x
            return False, None
        if pos_y < y_min:
            # overshot y
            return False, None


def main():
    input = [l.strip() for l in readlines()][0]
    v = [x.replace('x=', '').replace('y=', '') for x in input[13:].split(', ')]
    x_min, x_max = [int(x) for x in v[0].split('..')]
    y_min, y_max = [int(x) for x in v[1].split('..')]
    
    max_y = float('-inf')
    for x in range(0, x_min + 1):
        # lol -- wut r my constraints????
        for y in range(0, 1000):
            success, this_max_y = simulate(x, y, x_min, x_max, y_min, y_max)
            if success:
                max_y = max(max_y, this_max_y)

    print(max_y)

if __name__ == '__main__':
    main()
