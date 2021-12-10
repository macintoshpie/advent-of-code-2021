from python_utils import readlines
from itertools import permutations
from copy import deepcopy


def is_lowpoint(m, i, j):
    if m[i][j] == 'x':
        return False

    for horiz_delta, vert_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_i = i + vert_delta
        neighbor_j = j + horiz_delta
        if neighbor_i < 0 or neighbor_i >= len(m):
            continue
        elif neighbor_j < 0 or neighbor_j >= len(m[i]):
            continue
        elif m[neighbor_i][neighbor_j] == 'x':
            continue
        elif m[neighbor_i][neighbor_j] < m[i][j]:
            return False

    return True


def fill_basin(m, i, j, visited):
    if (i, j) in visited:
        return
    if i < 0 or i >= len(m):
        return
    if j < 0 or j >= len(m[i]):
        return
    if m[i][j] == 9:
        return

    if is_lowpoint(m, i, j):
        m[i][j] = 'x'
        visited.add((i, j))
        fill_basin(m, i, j-1, visited)
        fill_basin(m, i, j+1, visited)
        fill_basin(m, i-1, j, visited)
        fill_basin(m, i+1, j, visited)

def main():
    input = [l.strip() for l in readlines()]
    
    m = []
    for line in input:
        m.append([int(v) for v in line])

    visited = set()
    basins = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            m2 = deepcopy(m)
            fill_basin(m2, i, j, visited)
            basin_size = 0
            for row in m2:
                for val in row:
                    if val == 'x':
                        basin_size += 1
            if basin_size > 0:
                basins.append(basin_size)

    print(sorted(basins, reverse=True))
    a, b, c = sorted(basins, reverse=True)[:3]
    
    print(a * b * c)

if __name__ == '__main__':
    main()
