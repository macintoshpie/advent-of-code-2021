from day_01_part_01 import count_increases
from python_utils import readlines

def main():
    input = [int(v) for v in readlines()]
    groups = zip(input[:-2], input[1:-1], input[2:])
    sums = [
        sum(window)
        for window in groups
    ]
    print(count_increases(sums))

if __name__ == '__main__':
    main()
