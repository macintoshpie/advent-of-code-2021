from __future__ import annotations
from typing import Any
from python_utils import readlines
from collections import defaultdict, namedtuple
from itertools import combinations
from pprint import pprint
from copy import deepcopy


class Scanner:
    def __init__(self, id, readings: list[Reading]):
        self.id = id
        self.readings = readings

    def __repr__(self) -> str:
        return f'Scanner {self.id} {self.readings}'

Reading = namedtuple('Reading', ['x', 'y', 'z'])

def parse_input(lines):
    scanners: list[Scanner] = []
    current_scanner_idx = -1
    current_readings = []
    for line in lines:
        if not line:
            continue
        if '---' in line:
            if current_readings:
                scanners.append(Scanner(current_scanner_idx, current_readings))
                current_readings = []
            current_scanner_idx += 1
        else:
            values = line.split(',')
            current_readings.append(Reading(*[int(v) for v in values]))

    scanners.append(Scanner(current_scanner_idx, current_readings))

    return scanners


"""
    x
    |
    |
    |
    |___________z
   /
  /
 /
y
"""
def rotate_z(r: Reading, n: int) -> Reading:
    x, y, z = r.x, r.y, r.z
    for _ in range(n):
        tmp_y = x
        tmp_x = -1 * y

        x, y, z = tmp_x, tmp_y, z

    return Reading(x, y, z)

def rotate_x(r: Reading, n: int) -> Reading:
    x, y, z = r.x, r.y, r.z
    for _ in range(n):
        tmp_z = y
        tmp_y = -1 * z

        x, y, z = x, tmp_y, tmp_z
        
        
    return Reading(x, y, z)

def rotate_y(r: Reading, n: int) -> Reading:
    x, y, z = r.x, r.y, r.z
    for _ in range(n):
        tmp_x = z
        tmp_z = -1 * x

        x, y, z = tmp_x, y, tmp_z

    return Reading(x, y, z)


def transform(r: Reading, rotations, trans_x, trans_y, trans_z):
    for rotation in rotations:
        r = rotation(r, 1)

    return Reading(r.x + trans_x, r.y + trans_y, r.z + trans_z)

def get_mapping(scanner_a: Scanner, scanner_b: Scanner):
    for sample_b in scanner_b.readings:
        for sample_a in scanner_a.readings:
            # each pattern contains:
            #  1) an "initialization" rotation (i.e. having a single face start at 6 cardinal starting directions)
            #  2) a rotation which should be repeated 4 times to cover all rotations
            patterns = [
                ([], rotate_y),
                ([rotate_z], rotate_x),
                ([rotate_z, rotate_z], rotate_y),
                ([rotate_z, rotate_z, rotate_z], rotate_x),
                ([rotate_x], rotate_z),
                ([rotate_x, rotate_x, rotate_x], rotate_z),
            ]
            for pattern in patterns:
                initers = pattern[0]
                repeater = pattern[1]
                # print('New orientation...')
                for i in range(4):
                    rotations = initers + ([repeater] * i)
                    rotated_b = sample_b
                    for rotation in rotations:
                        rotated_b = rotation(rotated_b, 1)
                    # print('Rotated b: ', rotated_b)

                    trans_x = sample_a.x - rotated_b.x
                    trans_y = sample_a.y - rotated_b.y
                    trans_z = sample_a.z - rotated_b.z
                    
                    # now we know how to rotate and translate the points from b to a
                    successful_matches = 0
                    for point_b in scanner_b.readings:
                        mapped_b = transform(point_b, rotations, trans_x, trans_y, trans_z)
                        if mapped_b in scanner_a.readings:
                            successful_matches += 1
                    
                    if successful_matches >= 12:
                        # we found a mapping from b to a!
                        
                        return rotations, (trans_x, trans_y, trans_z)

    return None, None


def find_path(graph, start, end, visited, path):
    if start == end:
        # found the end
        return path

    for neighbor in graph[start].keys():
        if neighbor not in visited:
            new_visited = deepcopy(visited)
            new_visited.add(neighbor)
            found_path = find_path(graph, neighbor, end, new_visited, path + [neighbor])
            if found_path is not None:
                return found_path
    
    return None


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
    
    all_readings = set(scanners[0].readings)
    for i in range(1, len(scanners)):
        # transform scanner i's readings relative to scanner zero and add to our set
        path = find_path(transformations, i, 0, set(), [])
        print(f'{i} -> {0}: {path}')

        source_id = i
        current_readings = scanners_by_id[source_id].readings
        for dest_id in path:
            transformed_readings = []
            # map from source to dest
            rotations, trans = transformations[source_id][dest_id]
            for current_beacon in current_readings:
                transformed_readings.append(transform(current_beacon, rotations, trans[0], trans[1], trans[2]))
            
            current_readings = transformed_readings
            source_id = dest_id
        
        for transformed_beacon in current_readings:
            all_readings.add(transformed_beacon)

    print(len(all_readings))

if __name__ == '__main__':
    main()
