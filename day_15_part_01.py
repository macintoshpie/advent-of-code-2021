from __future__ import annotations
from heapq import heapify, heappop, heappush
from python_utils import readlines


def parse_input(lines: list[list[str]]):
    graph = []
    for i, row in enumerate(lines):
        graph_row = []
        for j, cost in enumerate(list(row)):
            graph_row.append(int(cost))

        graph.append(graph_row)
    
    return graph


def get_valid_neighbors(node_idx, max_row, max_col):
    neighbors = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = node_idx[0] + i
        new_col = node_idx[1] + j
        if (
            new_row < 0 or new_col < 0
            or new_row > max_row or new_col > max_col
        ):
            continue
        neighbors.append((new_row, new_col))

    return neighbors


def dijkstra(graph, start_idx, end_idx):
    # source! https://gist.github.com/kachayev/5990802
    max_row, max_col = len(graph) - 1, len(graph[0]) - 1
    seen = set()
    q = [(0, start_idx, ())]
    min_costs = {start_idx: 0}
    while q:
        cost, node_idx, path = heappop(q)
        if node_idx not in seen:
            seen.add(node_idx)
            path = (node_idx, path)

            if node_idx == end_idx:
                return (cost, path)
            
            for neighbor_idx in get_valid_neighbors(node_idx, max_row, max_col):
                if neighbor_idx in seen:
                    continue

                current_cost = min_costs.get(neighbor_idx, float('inf'))
                neighbor_cost = graph[neighbor_idx[0]][neighbor_idx[1]]
                new_cost = neighbor_cost + cost
                if new_cost < current_cost:
                    min_costs[neighbor_idx] = new_cost
                    heappush(q, (new_cost, neighbor_idx, path))


def main():
    input = [l.strip() for l in readlines()]
    
    graph = parse_input(input)
    start, end = (0, 0), (len(graph) - 1, len(graph[0]) - 1)
    cost, path = dijkstra(graph, start, end)
    print(cost)

if __name__ == '__main__':
    main()
