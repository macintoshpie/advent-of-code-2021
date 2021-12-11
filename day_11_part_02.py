from python_utils import readlines
from day_11_part_01 import increment


def main():
    input = [[int(v) for v in l.strip()] for l in readlines()]
    
    current_state = input
    total_octopi = len(current_state) * len(current_state[0])
    total_flash_count = None
    step_number = 0
    while total_flash_count != total_octopi:
        step_number += 1
        total_flash_count = 0
        # increment and flash all cells
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                flashes = increment(current_state, i, j)
                total_flash_count += flashes

        # reset all flashes
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] > 9:
                    current_state[i][j] = 0

    print(step_number)


if __name__ == '__main__':
    main()
