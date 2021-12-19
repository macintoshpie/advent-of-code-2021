from __future__ import annotations
from itertools import combinations
from typing import Any
from day_19_part_01 import transform, parse_input, get_mapping, find_path, Reading
from python_utils import readlines
from collections import defaultdict
from pprint import pprint


def man_dist(a, b):
    return sum([
        abs(a[0] - b[0]),
        abs(a[1] - b[1]),
        abs(a[2] - b[2]),
    ])

def main():
    input = [l.strip() for l in readlines()]
    scanners = parse_input(input)
    print(scanners)
    scanners_by_id = {
        scanner.id: scanner for scanner in scanners
    }

    transformations = defaultdict(dict)
    successfully_mapped_scanner_ids = [0]
    newly_mapped_scanners = [scanners_by_id[0]]
    while len(successfully_mapped_scanner_ids) < len(scanners):
        # for scanner_a, scanner_b in combinations(scanners, 2):
        next_mapped_scanners = []
        for newly_mapped_scanner in newly_mapped_scanners:
            for scanner in scanners:
                if scanner.id in successfully_mapped_scanner_ids:
                    continue
                
                rotations, translations = get_mapping(newly_mapped_scanner, scanner)
                if rotations is not None:
                    transformations[scanner.id][newly_mapped_scanner.id] = (rotations, translations)
                    successfully_mapped_scanner_ids.append(scanner.id)
                    print(f'Done with {len(successfully_mapped_scanner_ids)}')
                    next_mapped_scanners.append(scanner)

        newly_mapped_scanners = next_mapped_scanners

    pprint(transformations)

    scanner_positions = [(0, 0, 0)]
    for i in range(1, len(scanners)):
        # transform scanner i's readings relative to scanner zero and add to our set
        path = find_path(transformations, i, 0, set(), [])
        print(f'{i} -> {0}: {path}')

        source_id = i
        current_pos = Reading(0, 0, 0)
        for dest_id in path:
            # map from source to dest
            rotations, trans = transformations[source_id][dest_id]
            current_pos = transform(current_pos, rotations, trans[0], trans[1], trans[2])
            source_id = dest_id

        scanner_positions.append(current_pos)

    max_dist = -1
    for a, b in combinations(scanner_positions, 2):
        max_dist = max(max_dist, man_dist(a, b))

    print(scanner_positions)
    print(max_dist)

if __name__ == '__main__':
    main()
