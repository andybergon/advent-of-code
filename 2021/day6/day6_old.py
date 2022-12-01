
NEW_N_VALUE = 8


def load(filename):
    with open(filename) as f:
        line = f.readline()
        return [int(n) for n in line.split(',')]


def next_num(n):
    if n == 0:
        return 6, True
    else:
        return n - 1, False


def next_day(l):
    nd_list = []
    new_to_add = 0
    for n in l:
        next_n, add_new = next_num(n)
        if add_new:
            new_to_add += 1
        nd_list.append(next_n)
    nd_list.extend([NEW_N_VALUE] * new_to_add)
    return nd_list


def day_nth(l, nth=80):
    for i in range(nth):
        l = next_day(l)
    return l


def part_one(filename):
    l = load(filename)
    l = day_nth(l, nth=80)
    print(len(l))


def part_two(filename):
    l = load(filename)
    l = day_nth(l, nth=256)
    print(len(l))


part_one('day6.txt')  # 380758 # 10 min
# part_two('day6test.txt') # too slow
