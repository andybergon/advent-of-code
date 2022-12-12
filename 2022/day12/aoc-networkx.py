import networkx as nx

from aoc import find, find_all, get_grid, get_visitables


def build_graph(grid):
    G = nx.DiGraph()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curr = (i, j)
            for visitable in get_visitables(grid, curr):
                G.add_edge(curr, visitable)
    return G


def solution(is_sample=False):
    grid = get_grid(is_sample)

    start = find(grid, "S")
    end = find(grid, "E")

    G = build_graph(grid)

    path_len = len(nx.shortest_path(G, start, end))
    print(path_len - 1)

    starts = [start, *find_all(grid, "a")]
    paths_len = [len(nx.shortest_path(G, s, end)) for s in starts if nx.has_path(G, s, end)]
    print(min(paths_len) - 1)


if __name__ == "__main__":
    solution(False)
