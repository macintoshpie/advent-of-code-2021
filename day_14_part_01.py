from typing import DefaultDict
from python_utils import readlines
import re
from copy import deepcopy


def parse_input(lines: list[str]) -> tuple[str, list[tuple[str, str]]]:
    template = lines[0]
    rules = []
    for line in lines[2:]:
        x, y = line.split(' -> ')
        rules.append((x, y))

    return template, rules


def main():
    input = [l.strip() for l in readlines()]

    template, rules = parse_input(input)

    current_template = list(template)
    for _ in range(10):
        next_template = deepcopy(current_template)
        all_matches = []
        for rule in rules:
            matches = [m.start() for m in re.finditer(f'(?={rule[0]})', ''.join(current_template))]
            for match in matches:
                all_matches.append((match + 1, rule[1]))
        
        sorted_matches = sorted(all_matches, key=lambda x: x[0], reverse=True)
 
        for match in sorted_matches:
            next_template.insert(match[0], match[1])
        
        current_template = next_template

    counts = DefaultDict(lambda: 0)
    for char in current_template:
        counts[char] += 1

    min_count = float('inf')
    max_count = -1
    for key, count in counts.items():
        if count < min_count:
            min_count = count
        if count > max_count:
            max_count = count

    print(max_count - min_count)

if __name__ == '__main__':
    main()
