from __future__ import annotations
from typing import Dict

from python_utils import readlines


class Node:
    def __init__(self, label_: str):
        self.label = label_
        self.is_large = label_.upper() == label_
        self.neighbors: list[Node] = []
        self.visited = False

    def add_neighbor(self, node: Node) -> None:
        self.neighbors.append(node)


    @staticmethod
    def parse_graph(adjacency_lines: list[str]) -> Dict[str, Node]:
        nodes_by_label: dict[str, Node] = {}
        for line in adjacency_lines:
            a_label, b_label = line.split('-')
            a_node, b_node = nodes_by_label.get(a_label), nodes_by_label.get(b_label)
            if not a_node:
                a_node = Node(a_label)
                nodes_by_label[a_label] = a_node
            if not b_node:
                b_node = Node(b_label)
                nodes_by_label[b_label] = b_node

            a_node.add_neighbor(b_node)
            b_node.add_neighbor(a_node)
        
        return nodes_by_label

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.label == other.label

    @property
    def visitable(self):
        return self.is_large or not self.visited

    def get_paths(self, other: Node, paths_to_get_here: list[list[Node]]) -> list[list[Node]]:
        if self == other:
            return paths_to_get_here

        self.visited = True

        paths_to_other: list[list[Node]] = []
        for neighbor in self.neighbors:
            if neighbor.visitable:
                neighbor.visited = True

                paths_to_neighbor = [path + [neighbor] for path in paths_to_get_here]
                paths_to_end = neighbor.get_paths(other, paths_to_neighbor)
                for path in paths_to_end:
                    if path and path[-1] == other:
                        # successfully made it to the end
                        paths_to_other.append(path)

                neighbor.visited = False

        return paths_to_other

def main():
    input = [l.strip() for l in readlines()]

    nodes_by_label = Node.parse_graph(input)
    start_node = nodes_by_label['start']
    end_node = nodes_by_label['end']

    paths = start_node.get_paths(end_node, [[start_node]])
    print(len(paths))


if __name__ == '__main__':
    main()