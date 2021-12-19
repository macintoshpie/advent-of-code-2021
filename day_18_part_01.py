from __future__ import annotations
from typing import Union
from python_utils import readlines
import math

class Node:
    def __init__(self, left: Union[None, Node] = None, right: Union[None, Node] = None, value: Union[None, int] = None):
        self.left = left
        self.right = right
        assert (left and right) or value is not None
        self.value = value

    @property
    def magnitude(self):
        if self.is_terminal:
            return self.value

        return (self.left.magnitude * 3) + (self.right.magnitude * 2)

    def __repr__(self) -> str:
        if self.is_terminal:
            return str(self.value)
        return f'[{self.left}, {self.right}]'

    @property
    def is_terminal(self):
        return self.value is not None

    def to_terminal(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add_value(self, value):
        assert self.is_terminal
        self.value += value

    def split(self):
        assert self.is_terminal
        value = self.value
        self.value = None
        self.left = Node(value=math.floor(value / 2))
        self.right = Node(value=math.ceil(value / 2))

    def add(self, other: Node) -> Node:
        new_node = Node(self, other)
        return new_node

    def copy(self):
        if self.is_terminal:
            return Node(value=self.magnitude)
        return Node(left=self.left.copy(), right=self.right.copy())


def parse_pair(pair):
    a, b = pair
    if isinstance(a, int):
        left = Node(value=a)
    else:
        left = parse_pair(a)
    if isinstance(b, int):
        right = Node(value=b)
    else:
        right = parse_pair(b)

    node_pair = Node(left, right)

    return node_pair


def parse_input(lines) -> list[Node]:
    pairs = []
    for pair in lines:
        pairs.append(parse_pair(pair))

    return pairs

def find_explodable(node: Node, depth: int, explodable_node: Union[None, Node], prior_terminal_node: Union[None, Node]):
    if node.is_terminal:
        if explodable_node:
            # final terminal condition -- found previous and next values for the explodable node
            return explodable_node, prior_terminal_node, node
        else:
            return None, node, None

    if depth == 4 and not explodable_node:
        # found the first explodable node
        return node, prior_terminal_node, None

    found, prior, next_ = find_explodable(node.left, depth + 1, explodable_node, prior_terminal_node)
    if found:
        explodable_node = found
        if next_:
            return found, prior, next_
        else:
            # continue searching for the next!
            pass

    if prior:
        prior_terminal_node = prior

    found, prior, next_ = find_explodable(node.right, depth + 1, explodable_node, prior_terminal_node)
    if found:
        return found, prior, next_

    # didn't find anything explodable in subtree
    return None, prior, None


def explode_node(node, prior, next):
    node_left_value, node_right_value = node.left.value, node.right.value

    # this node turns into a zero
    node.to_terminal(0)
    
    # update the neighbors
    if prior is not None:
        prior.add_value(node_left_value)
    if next is not None:
        next.add_value(node_right_value)


def find_splittable(node: Node) -> Union[None, Node]:
    if node.is_terminal:
        if node.value >= 10:
            return node
        else:
            return None

    found = find_splittable(node.left)
    if found:
        return found
    found = find_splittable(node.right)
    if found:
        return found
    
    return None


def reduce(node: Node):
    reduced = True
    while reduced:
        reduced = False

        explodable_node, prior, next_ = find_explodable(node, 0, None, None)
        if explodable_node:
            explode_node(explodable_node, prior, next_)
            reduced = True
            continue
        
        splittable_node = find_splittable(node)
        if splittable_node:
            splittable_node.split()
            reduced = True
            continue



def main():
    input = [l.strip() for l in readlines()]
    all_lines = [eval(line) for line in input]
    all_pairs = parse_input(all_lines)
    print(all_pairs)
    
    current_pair = all_pairs[0]
    for pair in all_pairs[1:]:
        current_pair = current_pair.add(pair)
        reduce(current_pair)

    print('Final Result: ', current_pair)
    print(current_pair.magnitude)

if __name__ == '__main__':
    main()
