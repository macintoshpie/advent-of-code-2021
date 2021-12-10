from python_utils import readlines
from itertools import permutations
from copy import deepcopy

#  1111  
# 2    3
# 2    3
#  4444
# 5    6
# 5    6
#  7777

MAPPING = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
}

LIT_MAPPING = {
    (1, 2, 3, 5, 6, 7): 0,
    (3, 6): 1,
    (1, 3, 4, 5, 7): 2,
    (1, 3, 4, 6, 7): 3,
    (2, 3, 4, 6): 4,
    (1, 2, 4, 6, 7): 5,
    (1, 2, 4, 5, 6, 7): 6,
    (1, 3, 6): 7,
    (1, 2, 3, 4, 5, 6 ,7): 8,
    (1, 2, 3, 4, 6 ,7): 9,
}

CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def translate(chars, modified_mapping):
    lit = set()
    for char in chars:
        lit.add(MAPPING[modified_mapping[char]])

    lit = tuple(sorted(list(lit)))
    return LIT_MAPPING.get(lit, None)

def all_possible_mappings():
    return [dict(zip(CHARS, p)) for p in permutations(CHARS)]


def main():
    input = [l.strip() for l in readlines()]
    input = [l.split('|') for l in input]
    
    total_out = 0
    for signal_raw, output_raw in input:
        signals = signal_raw.split(' ')

        correct_translation = None
        all_mappings = (dict(zip(CHARS, p)) for p in permutations(CHARS))
        for mapping in all_mappings:
            translation = {}
            for signal in signals:
                value = translate(signal, mapping)
                if value == None:
                    break
                else:
                    translation[tuple(sorted(signal))] = value

            if len(translation) == 10:
                correct_translation = translation
                break

        out = []
        out_signals = [x for x in output_raw.split(' ') if x]
        for out_signal in out_signals:
            fixed_out_signal = tuple(sorted(out_signal))
            out.append(correct_translation[fixed_out_signal])
        
        out_int = int(''.join([str(v) for v in out]))
        total_out += out_int

    print(total_out)
    


if __name__ == '__main__':
    main()
