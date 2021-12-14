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


def most_minus_least(t, i, steps):
    for _ in range(steps):
        t = apply_step(t, i)

    c = Counter(t)
    freq = c.most_common()
    return freq[0][1] - freq[-1][1]


def part_one(filename):
    t, i = load(filename)
    r = most_minus_least(t, i, steps=10)
    print(r)


def part_two(filename):
    t, l = load(filename)
    r = most_minus_least(l, steps=10)
    print(r)


if __name__ == '__main__':
    part_one('day14.txt')  # 3555 # 15 min
    # part_two('day14test.txt')  # ? # ? min
