def load(filename):
    m = []
    with open(filename) as f:
        for row in f:
            m.append([int(a) for a in row.strip()])
    return m


def update_state(m, increments):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = m[i][j] + increments[i][j]


def update_increments(m, p, increments):
    i, j = p
    offsets = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for oi, oj in offsets:
        ii = i + oi
        jj = j + oj
        if 0 <= ii < len(m) and 0 <= jj < len(m[0]):
            if m[ii][jj] != 0:  # already blinked this iteration
                increments[ii][jj] = increments[ii][jj] + 1


def should_continue(m, flashed):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > 9 and not(flashed[i][j]):
                return True
    return False


def print_matrix(m):
    for i in range(len(m)):
        print(''.join([str(e) for e in m[i]]))
    print('=' * len(m[i]))


def count_step_flashes(m):
    c = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > 9:
                c += 1
                m[i][j] = 0
    return c


def count_iteration_flashes(m):
    c = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = m[i][j] + 1

    flashed = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
    while should_continue(m, flashed):
        increments = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] > 9 and not (flashed[i][j]):
                    update_increments(m, (i, j), increments)
                    flashed[i][j] = True
        update_state(m, increments)
    c += count_step_flashes(m)
    return c


def sum_flashes(m, iterations=100):
    s = 0
    for i in range(iterations):
        c = count_iteration_flashes(m)
        s += c
    return s


def part_one(filename):
    m = load(filename)
    c = sum_flashes(m)
    print(c)


def part_two(filename):
    l = load(filename)
    print(l)


part_one('day11.txt')  # ? (test = 1656) # ? min
# part_two('day11test.txt')  # ? # ? min
