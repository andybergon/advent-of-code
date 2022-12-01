import operator
from functools import partial


def first():
    pos_to_occs = {}  # actually no need to count also negatives
    l = load()
    for e in l:
        pos = 0
        for _ in e:
            el_occ = pos_to_occs.get(pos)
            if el_occ:
                unit_occ = (1, 0) if e[pos] == '0' else (0, 1)
                new_el_occ = tuple(map(operator.add, el_occ, unit_occ))
                pos_to_occs[pos] = new_el_occ
            else:
                pos_to_occs[pos] = (0, 0)
            pos += 1
    print(pos_to_occs)

    most_str = ''
    for i in range(0, len(pos_to_occs)):
        v = pos_to_occs[i]
        most_str += '0' if v[0] > v[1] else '1'
    most_int = int(most_str, 2)
    print(most_int)
    least_int = (2 ** len(pos_to_occs) - 1 - most_int)
    print(least_int)
    print(f'mult: {most_int * least_int}')


def second():
    l = load()
    el_len = len(l[0])

    pos = 0
    while len(l) > 1 and pos < el_len:
        l = filter_readings(l, pos, most=True)
        pos += 1
    most = int(l[0], 2)

    l = load()
    pos = 0
    while len(l) > 1 and pos < el_len:
        l = filter_readings(l, pos, most=False)
        pos += 1
    least = int(l[0], 2)

    print(f'most: {most} - least {least} - product: {most * least}')


def filter_readings(l, pos, most=True):
    zeroes = sum(1 for _ in filter(partial(filter_reading, position=pos, expected='0'), l))
    # tiebreakers: 1 for most, 0 for least
    most_exp = '0' if zeroes > len(l) / 2 else '1'
    least_exp = '0' if zeroes <= len(l) / 2 else '1'
    exp = most_exp if most else least_exp
    fun = partial(filter_reading, expected=exp)
    return list(filter(partial(fun, position=pos), l))


def filter_reading(reading, position, expected):
    return reading[position] == expected


def load(filename='/Users/abergonzo/Downloads/day3.txt'):
    with open(filename, 'r') as f:
        return [curr.strip() for curr in f]


if __name__ == '__main__':
    # first()
    second()
