from __future__ import annotations
from heapq import heappop, heappush
import math
from python_utils import readlines
from day_15_part_01 import parse_input, get_valid_neighbors


def get_cost(graph, i, j):
    num_rows = len(graph)
    num_cols = len(graph[0])
    tile_row = math.floor(i / num_rows)
    tile_col = math.floor(j / num_cols)
    cost = graph[i % num_rows][j % num_cols] + tile_row + tile_col
    if cost <= 9:
        return cost
    else:
        return cost % 9


def dijkstra(graph, start_idx, end_idx):
    # source! https://gist.github.com/kachayev/5990802
    max_row, max_col = (len(graph) * 5) - 1, (len(graph[0]) * 5) - 1
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
                neighbor_cost = get_cost(graph, neighbor_idx[0], neighbor_idx[1])
                new_cost = neighbor_cost + cost
                if new_cost < current_cost:
                    min_costs[neighbor_idx] = new_cost
                    heappush(q, (new_cost, neighbor_idx, path))

    return (None, ())


def main():
    input = [l.strip() for l in readlines()]
    
    graph = parse_input(input)
    start, end = (0, 0), ((len(graph) * 5) - 1, (len(graph[0]) * 5) - 1)
    print(start, end)
    cost, path = dijkstra(graph, start, end)
    print(cost)


if __name__ == '__main__':
    main()
