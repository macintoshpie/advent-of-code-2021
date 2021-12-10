from python_utils import readlines
from itertools import permutations
from copy import deepcopy


def is_lowpoint(m, i, j):
    for horiz_delta in [-1, 0, 1]:
        for vert_delta in [-1, 0, 1]:
            if horiz_delta == 0 and vert_delta == 0:
                continue
            
            new_i = i + vert_delta
            new_j = j + horiz_delta
            if new_i < 0 or new_i >= len(m):
                continue
            elif new_j < 0 or new_j >= len(m[i]):
                continue
            elif m[new_i][new_j] <= m[i][j]:
                return False
    
    return True

def main():
    input = [l.strip() for l in readlines()]
    
    m = []
    for line in input:
        m.append([int(v) for v in line])
    
    lowpoints = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if is_lowpoint(m, i, j):
                lowpoints.append(m[i][j])

    print(sum(lowpoints) + (len(lowpoints)))

if __name__ == '__main__':
    main()
