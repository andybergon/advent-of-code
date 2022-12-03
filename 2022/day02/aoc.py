def value(e):
    # ord('a') -> 97 | 1-26
    # ord('A') -> 65 | 27-52
    if e.isupper():
        return ord(e) - (65 - 27)
    else:
        return ord(e) - (97 - 1)


def part_one(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            row = row.strip()
            i = len(row) // 2
            first, second = row[:i], row[i:]
            s = set(first)
            for e in second:
                if e in s:
                    l.append(e)
                    break
    print(l)
    print(sum([value(e) for e in l]))
    return l


def part_two(is_sample=False):
    l = []
    priorities = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            l.append(row.strip())
    groups = list(partition(l, 3))
    print(groups)

    for group in groups:
        common = set(group[0])
        for elf in group[1:]:
            common = common.intersection(set(elf))
        priorities.append(common)
    print(priorities)
    # min({'a'} is an easy to get single element
    print(sum([value(min(e)) for e in priorities]))


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_filename(is_sample=False):
    return 'input_sample.txt' if is_sample else 'input.txt'


if __name__ == '__main__':
    # part_one(False)  # ? # 10 min
    part_two(False)  # ? # 12 min
