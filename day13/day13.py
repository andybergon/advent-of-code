import numpy as np


def load(filename):
    l = []
    folds = []
    with open(filename) as f:
        for row in f:
            if row == '\n':
                continue
            elif row.startswith('fold along'):
                ax, am = row.strip().replace('fold along ', '').split('=')
                folds.append((ax == 'x', int(am)))  # x == 0, y == 1
            else:
                j, i = row.strip().split(',')  # x,y
                l.append((int(i), int(j)))
    return l, folds


def max_ij(l):
    # could iterate once
    return max(map(lambda t: t[0], l)), max(map(lambda t: t[1], l))


def create_matrix(l):
    max_i, max_j = max_ij(l)
    m = [[False for _ in range(max_j + 1)] for _ in range(max_i + 1)]
    for i, j in l:
        m[i][j] = True
    return m


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            ch = '#' if m[i][j] else '.'
            print(ch, end='')
        print()


def merge(half_stay, half_flipped):
    m = []
    for i in range(len(half_stay)):
        row = []
        for j in range(len(half_stay[i])):
            row.append(half_stay[i][j] or half_flipped[i][j])
        m.append(row)
    return m


def flip(m, ax):
    return np.flip(np.array(m), axis=ax)


def fold(m, fold):
    ax, am = fold
    m_np = np.array(m)
    half_const, half_to_flip = np.split(m_np, [am], ax)
    half_flipped = flip(half_to_flip, ax)
    return merge(half_const, half_flipped)


def apply_all_folds(m, folds):
    for f in folds:
        m = fold(m, f)
    return m


def count_hashes(m):
    c = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]:
                c += 1
    return c


def part_one(filename):
    l, folds = load(filename)
    m = create_matrix(l)
    # print_m(m)
    m = fold(m, folds[0])
    # print('=' * 20)
    # print_m(m)
    c = count_hashes(m)
    print(c)


def part_two(filename):
    l, folds = load(filename)
    m = create_matrix(l)
    m = apply_all_folds(m, folds)
    print_m(m)


if __name__ == '__main__':
    # part_one('day13.txt')  # 775 # 1h
    part_two('day13.txt')  # ? # ? min
