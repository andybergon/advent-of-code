import math
from copy import deepcopy

ij_offsets = (-1, 0), (0, 1), (1, 0), (0, -1)
ij_offsets_dr = (0, 1), (1, 0)


def load(filename):
    m = []
    with open(filename) as f:
        for line in f:
            m.append([int(e) for e in line.strip()])
    return m


def neighs_to_visit(m, p, visited):
    neighs = []
    for (ii, jj) in [(i + p[0], j + p[1]) for i, j in ij_offsets_dr]:
        if 0 <= ii < len(m) and 0 <= jj < len(m[0]) and not visited[ii][jj]:
            neighs.append((ii, jj))
    sorted_neighs = sorted(neighs, key=lambda ij: m[ij[0]][ij[1]])
    return sorted_neighs


def lowest_risk(m):
    costs = [[math.inf for _ in range(len(m[0]))] for _ in range(len(m))]
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    lowest_risk_rec(m, (0, 0), costs, 0, visited)
    return costs[-1][-1]


def print_path(path):
    print('->'.join([str(s) for s in path]))


def lowest_risk_rec(m, p, costs, cost, visited):
    i, j = p
    costs[i][j] = cost
    visited[i][j] = True
    if p == (len(m) - 1, len(m[0]) - 1):
        # print(cost)
        return
    else:
        neighs = neighs_to_visit(m, p, visited)
        for neigh in neighs:
            ni, nj = neigh
            new_cost = cost + m[ni][nj]
            if new_cost <= costs[ni][nj]:
                lowest_risk_rec(m, neigh, costs, new_cost, deepcopy(visited))


def part_one(filename):
    m = load(filename)
    r = lowest_risk(m)
    print(r)


def part_two(filename):
    m = load(filename)
    print(m)


if __name__ == '__main__':
    part_one('day15.txt')  # ? # 11:15 min
    # part_two('day15test.txt')  # ? # ? min
