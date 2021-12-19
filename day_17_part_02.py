from python_utils import readlines
from day_17_part_01 import simulate


def main():
    input = [l.strip() for l in readlines()][0]
    v = [x.replace('x=', '').replace('y=', '') for x in input[13:].split(', ')]
    x_min, x_max = [int(x) for x in v[0].split('..')]
    y_min, y_max = [int(x) for x in v[1].split('..')]
 
    num_hits = 0
    for x in range(0, x_max + 1):
        # lol -- wut r my constraints????
        for y in range(y_min - 1, 1000):
            success, _ = simulate(x, y, x_min, x_max, y_min, y_max)
            if success:
                num_hits += 1

    print(num_hits)

if __name__ == '__main__':
    main()
