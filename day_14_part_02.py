from collections import defaultdict
from python_utils import readlines
from copy import deepcopy


def template_to_dict(template):
    pairs = zip(template, template[1:])    
    result = defaultdict(lambda: 0)
    for pair in pairs:
        result[''.join(pair)] += 1

    return result


def main():
    input = [l.strip() for l in readlines()]

    template = input[0]
    rules = []
    for line in input[2:]:
        x, y = line.split(' -> ')
        rules.append((x, y))

    current_template = list(template)
    char_counts = defaultdict(lambda: 0)
    for char in current_template:
        char_counts[char] += 1

    current_template = template_to_dict(current_template)
    for _ in range(40):
        next_template = deepcopy(current_template)
        for rule in rules:
            pattern, new_char = rule
            if pattern in current_template:
                next_template[pattern[0]+new_char] += current_template[pattern]
                next_template[new_char+pattern[1]] += current_template[pattern]
                char_counts[new_char] += current_template[pattern]
                next_template[pattern] -= current_template[pattern]
    
        current_template = next_template

    print(max(char_counts.values()) - min(char_counts.values()))

if __name__ == '__main__':
    main()
