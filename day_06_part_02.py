from typing import DefaultDict
from python_utils import readlines

def main():
    input = [l.strip() for l in readlines()]

    all_fish = [int(v) for v in input[0].split(',')]
    fish_counts = DefaultDict(lambda: 0)
    for fish in all_fish:
        fish_counts[fish] += 1

    current_step = fish_counts
    num_days = 256
    for i in range(num_days):
        next_step = DefaultDict(lambda: 0)
        for fish, count in current_step.items():
            if fish == 0:
                next_step[6] += count
                next_step[8] += count
            else:
                next_step[fish - 1] += count

        current_step = next_step

    print(sum(current_step.values()))


if __name__ == '__main__':
    main()
