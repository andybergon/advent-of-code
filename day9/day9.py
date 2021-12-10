import math

ij_offsets = (-1, 0), (0, 1), (1, 0), (0, -1)


def load(filename):
    matrix = []
    with open(filename) as f:
        for row in f:
            matrix.append([int(d) for d in row.strip()])
    return matrix


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
            print((ipp,jpp))
    return l


def sum_from_neigh(m, neigh, visited):
    i, j = neigh
    visited[i][j] = True
    neighs = neighbours_to_consider(m, (i, j), visited)  # could just return 0 from recursive
    if neighs:
        for neigh in neighs:
            return 1 + sum_from_neigh(m, neigh, visited)
    else:
        return 0


def get_basin_sizes(m):
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    basin_sizes = []
    current_basin_size = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            is_lp = is_low_point(i, j, m)
            if is_lp:
                print('new LP')
                visited[i][j] = True
                current_basin_size += 1
                for neigh in neighbours_to_consider(m, (i, j), visited):
                    s = sum_from_neigh(m, neigh, visited)
                    current_basin_size += s
                basin_sizes.append(current_basin_size)
    return basin_sizes


def sum_top_basins(m):
    sizes = get_basin_sizes(m)
    print(sizes)
    return math.prod(sorted(sizes, reverse=True)[:3])


def sum_risk_levels(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            is_lp = is_low_point(i, j, m)
            if is_lp:
                # print(f'{m[i][j]} - {[safe_get(m, (i + ii, j + jj)) for ii, jj in [(-1, 0), (0, 1), (1, 0), (0, -1)]]}')
                s += m[i][j] + 1
    return s


def is_low_point(i, j, m):
    # could be reworked with offsets [(-1, 0), (0, 1), (1, 0), (0, -1)] and to exit early
    lt_up = safe_lt(m, (i, j), (i - 1, j))
    lt_right = safe_lt(m, (i, j), (i, j + 1))
    lt_down = safe_lt(m, (i, j), (i + 1, j))
    lt_left = safe_lt(m, (i, j), (i, j - 1))
    return lt_down and lt_left and lt_right and lt_up


def safe_get(m, ij):
    i, j = ij
    if i < 0 or j < 0:
        return None
    try:
        return m[i][j]
    except:
        return None


def safe_lt(m, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 < 0 or y2 < 0:
        return True
    else:
        try:
            return m[x1][y1] < m[x2][y2]
        except:
            return True


def part_one(filename):
    m = load(filename)
    s = sum_risk_levels(m)
    print(s)


def part_two(filename):
    m = load(filename)
    s = sum_top_basins(m)
    print(s)


# part_one('day10.txt')  # 633 # 15 min (+30 min debug m[-1] is not OOB)
part_two('day9test.txt')  # ? #
