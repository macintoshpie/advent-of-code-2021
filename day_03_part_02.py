from collections import namedtuple
from copy import deepcopy

from day_03_part_01 import bit_array_to_number
from python_utils import readlines


class BitFrequencyNode:
    def __init__(self):
        self.count = {
            True: 0,
            False: 0,
        }
        self.next = {
            True: None,
            False: None,
        }


def make_trie(current_node: BitFrequencyNode, num_bits: int) -> BitFrequencyNode:
    if not num_bits:
        return

    true_node = BitFrequencyNode()
    make_trie(true_node, num_bits - 1)
    false_node = BitFrequencyNode()
    make_trie(false_node, num_bits - 1)

    current_node.next[True] = true_node
    current_node.next[False] = false_node


def update_trie(current_node: BitFrequencyNode, bit_array: list[bool]) -> None:
    if not bit_array:
        return

    current_node.count[bit_array[0]] += 1
    update_trie(current_node.next[bit_array[0]], bit_array[1:])


def walk_to_construct_bit_array(current_node: BitFrequencyNode, eval_func: callable, default: bool) -> list[bool]:
    if not current_node:
        return []

    winner = None
    if current_node.count[True] == current_node.count[False]:
        winner = default
    elif current_node.count[True] == 0:
        winner = False
    elif current_node.count[False] == 0:
        winner = True
    else:
        winner = eval_func(current_node.count[True], current_node.count[False]) == current_node.count[True]

    return [winner] + walk_to_construct_bit_array(current_node.next[winner], eval_func, default)


def main():
    bit_arrays = [
        [bool(int(bit)) for bit in line.strip()]
        for line in readlines()
    ]
    num_bits = len(bit_arrays[0])

    ROOT = BitFrequencyNode()
    make_trie(ROOT, num_bits - 1)

    for bit_array in bit_arrays:
        update_trie(ROOT, bit_array)

    o2_bit_array = walk_to_construct_bit_array(ROOT, max, True)
    co2_bit_array = walk_to_construct_bit_array(ROOT, min, False)
    
    print(bit_array_to_number(o2_bit_array) * bit_array_to_number(co2_bit_array))


if __name__ == '__main__':
    main()
