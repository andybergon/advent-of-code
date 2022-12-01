import math

ij_offsets = (-1, 0), (0, 1), (1, 0), (0, -1)


def load(filename):
    matrix = []
    with open(filename) as f:
        for row in f:
            matrix.append([int(d) for d in row.strip()])
    return matrix


def safe_lt(m, p1, p2):
    i1, j1 = p1
    i2, j2 = p2
    if 0 <= i2 < len(m) and 0 <= j2 < len(m[0]):
        return m[i1][j1] < m[i2][j2]
    else:
        return True


def is_low_point(m, i, j):
    is_lp = True
    for ii, jj in ij_offsets:
        is_lp = is_lp and safe_lt(m, (i, j), (i + ii, j + jj))
    return is_lp


def sum_risk_levels(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            is_lp = is_low_point(m, i, j)
            if is_lp:
                # print(f'{m[i][j]} - {[safe_get(m, (i + ii, j + jj)) for ii, jj in [(-1, 0), (0, 1), (1, 0), (0, -1)]]}')
                s += m[i][j] + 1
    return s


def neighbours_to_consider(m, p, visited):
    l = []
    i, j = p
    for pp in [(i + ii, j + jj) for ii, jj in ij_offsets]:
        ipp, jpp = pp
        if 0 <= ipp < len(m) and 0 <= jpp < len(m[0]) \
                and not visited[ipp][jpp] \
                and safe_lt(m, (i, j), (ipp, jpp)) \
                and m[ipp][jpp] != 9:  # hack
            l.append((ipp, jpp))
            # print(f'{(ipp, jpp)} = {m[ipp][jpp]}')
    return l


def sum_from_neigh(m, p, visited):
    i, j = p
    if visited[i][j]:  # because neighbours could be not relevant anymore if reached by another path
        return 0
    else:
        visited[i][j] = True

    neighs = neighbours_to_consider(m, (i, j), visited)  # could just return 0 from recursive
    if neighs:
        c = 1
        for neigh in neighs:
            c += sum_from_neigh(m, neigh, visited)
        return c
    else:
        return 1


def get_basin_sizes(m):
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    basin_sizes = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            is_lp = is_low_point(m, i, j)
            if is_lp:
                # print(f'===> LP: {(i, j)} = {m[i][j]}')
                basin_sizes.append(sum_from_neigh(m, (i, j), visited))
                # print(f'==> Basin Size: {current_basin_size}')
    return basin_sizes


def sum_top_basins(m):
    sizes = get_basin_sizes(m)
    print(sizes)
    return math.prod(sorted(sizes, reverse=True)[:3])


def part_one(filename):
    m = load(filename)
    s = sum_risk_levels(m)
    print(s)


def part_two(filename):
    m = load(filename)
    s = sum_top_basins(m)
    print(s)


# part_one('day9.txt')  # 633 # 15 min (+30 min debug m[-1] is not OOB)
part_two('day9.txt')  # ? # 2h+ # correct for test: 9 * 14 * 9 = 1134
