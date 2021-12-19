from __future__ import annotations
from python_utils import readlines
from day_18_part_01 import parse_input, reduce

def main():
    input = [l.strip() for l in readlines()]
    all_lines = [eval(line) for line in input]
    all_pairs = parse_input(all_lines)
    print(all_pairs)
    
    largest_magnitude = -1
    for i in range(len(all_pairs)):
        for j in range(i + 1, len(all_pairs)):
            left = all_pairs[i].copy()
            right = all_pairs[j].copy()
            added = left.add(right)
            reduce(added)
            largest_magnitude = max(largest_magnitude, added.magnitude)
            
            left = all_pairs[j].copy()
            right = all_pairs[i].copy()
            added = left.add(right)
            reduce(added)
            largest_magnitude = max(largest_magnitude, added.magnitude)

    print(largest_magnitude)


if __name__ == '__main__':
    main()
