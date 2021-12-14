from collections import Counter


def load(filename):
    insertions = {}
    with open(filename) as f:
        template = f.readline().strip()
        f.readline()
        while row := f.readline():
            fr, to = row.strip().split(' -> ')
            insertions[fr] = to
    return template, insertions


def apply_step(t, i):
    new_t = ''
    prev = t[0]
    for ch in t[1:]:
        ins = i[prev + ch]
        new_t += prev + ins
        prev = ch
    new_t += prev
    return new_t


def apply_step_counter(tc, i):
    new_tc = Counter()
    for bi, count in tc.items():
        first, third = bi
        second = i[bi]
        c = Counter({first + second: count, second + third: count})
        # new_tc.update([first+second])
        # new_tc.update([second + third])
        new_tc.update(c)
    return new_tc


def pair_counter(t):
    tc = Counter()
    prev = t[0]
    for ch in t[1:]:
        tc.update([prev + ch])
        prev = ch
    return tc


def most_minus_least(t, i, steps):
    tc = pair_counter(t)
    for _ in range(steps):
        tc = apply_step_counter(tc, i)

    c = Counter()
    for bi, count in tc.items():
        c.update(Counter({bi[1]: count}))
        # c.update(Counter({bi[0]: count, bi[1]: count}))
    freq = c.most_common()
    return freq[0][1] - freq[-1][1]


def part_one(filename):
    t, i = load(filename)
    r = most_minus_least(t, i, steps=10)
    print(r)


def part_two(filename):
    t, i = load(filename)
    r = most_minus_least(t, i, steps=40)
    print(r)


if __name__ == '__main__':
    # part_one('day14.txt')  # 3555 # 15 min
    part_two('day14.txt')  # 4439442043739 # 15 min
