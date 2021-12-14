from typing import DefaultDict
from python_utils import readlines
from copy import deepcopy

from day_14_part_01 import parse_input


def count_pairs(template: str) -> DefaultDict[str, int]:
    pairs = zip(template, template[1:])    
    result: DefaultDict[str, int] = DefaultDict(lambda: 0)
    for pair in pairs:
        result[''.join(pair)] += 1

    return result


def main():
    input = [l.strip() for l in readlines()]
    template, rules = parse_input(input)

    char_counts = DefaultDict(lambda: 0)
    for char in template:
        char_counts[char] += 1

    current_pair_counts = count_pairs(template)
    for _ in range(40):
        next_pair_counts = deepcopy(current_pair_counts)
        for rule in rules:
            pattern, new_char = rule
            if pattern in current_pair_counts:
                next_pair_counts[pattern[0]+new_char] += current_pair_counts[pattern]
                next_pair_counts[new_char+pattern[1]] += current_pair_counts[pattern]
                char_counts[new_char] += current_pair_counts[pattern]
                next_pair_counts[pattern] -= current_pair_counts[pattern]
    
        current_pair_counts = next_pair_counts

    print(max(char_counts.values()) - min(char_counts.values()))

if __name__ == '__main__':
    main()
