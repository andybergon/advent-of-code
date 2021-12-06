def load(filename='/Users/abergonzo/Downloads/input.txt'):
    l = []
    with open(filename, 'r') as f:
        for curr in f:
            l.append(int(curr.strip()))
    return l


def second(n=3):
    lines, increments = 0, 0
    l = load()
    prev = None
    for i in range(len(l)):
        lines += 1
        curr = sum(l[i: i + n])
        if prev and curr > prev:
            increments += 1
        prev = curr

    print(f'Lines: {lines}')
    print(f'Increments: {increments}')


def first():
    lines, increments = 0, 0

    with open('/Users/abergonzo/Downloads/input.txt', 'r') as f:
        prev = None
        for curr in f:
            curr = int(curr.strip())
            lines += 1
            if prev and curr > prev:
                increments += 1
            prev = curr

        print(f'Lines: {lines}')
        print(f'Increments: {increments}')


second()
