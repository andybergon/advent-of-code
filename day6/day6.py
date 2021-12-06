from collections import Counter

NEW_N_VALUE = 8
RESET_N_VALUE = 6


def load(filename):
    with open(filename) as f:
        line = f.readline()
        l = [int(n) for n in line.split(',')]
        return Counter(l)


def next_num(n):
    if n == 0:
        return RESET_N_VALUE, True
    else:
        return n - 1, False


def next_day(c: Counter):
    new_c = Counter()
    new_to_add = 0
    for n, occ in c.items():
        next_n, add_new = next_num(n)
        new_c.update({next_n: occ})
        if add_new:
            new_to_add = occ
    if new_to_add:
        new_c.update({NEW_N_VALUE: new_to_add})
    return new_c


def day_nth(c, nth=80):
    for i in range(nth):
        c = next_day(c)
    return c


def part_one(filename):
    c = load(filename)
    c = day_nth(c, nth=80)
    print(sum(c.values()))


def part_two(filename):
    c = load(filename)
    c = day_nth(c, nth=256)
    print(sum(c.values()))


part_one('day6.txt')  # 380758 # 10 min
part_two('day6.txt')  # 1710623015163 # 20min (redo with counters instead of lists)
