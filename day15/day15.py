from copy import deepcopy

ij_offsets = (-1, 0), (0, 1), (1, 0), (0, -1)


def load(filename):
    m = []
    with open(filename) as f:
        for line in f:
            m.append([int(e) for e in line.strip()])
    return m


def neighs_to_visit(m, p, visited):
    neighs = []
    for (ii, jj) in [(i + p[0], j + p[1]) for i, j in ij_offsets]:
        if 0 <= ii < len(m) and 0 <= jj < len(m[0]) and not visited[ii][jj]:
            neighs.append((ii, jj))
    return neighs


def lowest_risk(m):
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    return lowest_risk_rec(m, (0, 0), visited)


def lowest_risk_rec(m, p, visited):
    i, j = p
    if p == (len(m) - 1, len(m[0]) - 1):
        return m[i][j]
    else:
        visited[i][j] = True
        neighs = neighs_to_visit(m, p, visited)
        if neighs:
            neigh_risks = []
            for neigh in neighs:
                lowest_r = lowest_risk_rec(m, neigh, deepcopy(visited))
                if lowest_r:
                    neigh_risks.append(m[i][j] + lowest_r)
            if neigh_risks:
                return min(neigh_risks)


def part_one(filename):
    m = load(filename)
    r = lowest_risk(m)
    print(r)


def part_two(filename):
    m = load(filename)
    print(m)


if __name__ == '__main__':
    part_one('day15test.txt')  # ? # 11:15 min
    # part_two('day15test.txt')  # ? # ? min
