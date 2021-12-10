import math

ij_offsets = (-1, 0), (0, 1), (1, 0), (0, -1)


def load(filename):
    matrix = []
    with open(filename) as f:
        for row in f:
            matrix.append([int(d) for d in row.strip()])
    return matrix


def neighbours_to_consider(m, p, in_basin):
    l = []
    i, j = p
    for pp in [(i + ii, j + jj) for ii, jj in ij_offsets]:
        ipp, jpp = pp
        if ipp >= 0 and jpp >= 0:
            if in_basin[ipp][jpp]:
                l.append(ipp, jpp)
    return l


def get_basin_sizes(m):
    in_basin = [[False * len(m)] * len(m)]
    basin_sizes = []
    current_basin_size = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            is_lp = is_low_point(i, j, m)
            if is_lp:
                in_basin[i][j] = True
                current_basin_size += 1
                for neigh in neighbours_to_consider(m, (i, j), in_basin):
                    pass  # TODO

    return basin_sizes


def sum_top_basins(m):
    b = get_basin_sizes(m)
    return math.prod(sorted(b, reverse=True)[:3])


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


# part_one('day9.txt')  # 633 # 15 min (+30 min debug m[-1] is not OOB)
part_two('day9test.txt')  # ? #
