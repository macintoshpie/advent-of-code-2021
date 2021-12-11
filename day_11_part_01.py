from python_utils import readlines


NUM_STEPS = 100


def increment(state: list[list[int]], i: int, j: int) -> int:
    if i < 0 or i >= len(state) or j < 0 or j >= len(state[i]):
        # out of bounds
        return 0

    if state[i][j] > 9:
        # already flashed
        return 0

    state[i][j] += 1
    if state[i][j] > 9:
        # triggered flash
        # increment neighbors
        neighbor_flashes = 0
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if m == 0 and n == 0:
                    # skip itself
                    continue
                neighbor_flashes += increment(state, i + m, j + n)
        return 1 + neighbor_flashes
    else:
        return 0


def main():
    input = [[int(v) for v in l.strip()] for l in readlines()]
    
    current_state = input
    total_flashes = 0
    for _ in range(NUM_STEPS):
        # increment and flash all cells
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                flashes = increment(current_state, i, j)
                total_flashes += flashes

        # reset all flashes
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] > 9:
                    current_state[i][j] = 0

    print(total_flashes)


if __name__ == '__main__':
    main()
