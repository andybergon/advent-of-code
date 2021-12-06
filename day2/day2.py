def second():
    h, v, aim = 0, 0, 0
    l = load()

    for t in l:
        command = t[0]
        amount = t[1]
        if command == 'forward':
            h += amount
            v += aim * amount
        elif command == 'down':
            # v += amount
            aim += amount
        elif command == 'up':
            # v -= amount
            aim -= amount
    print(f'h: {h} - v: {v} - h*v: {h * v} - aim: {aim}')


def load(filename='/Users/abergonzo/Downloads/input2.txt'):
    l = []
    with open(filename, 'r') as f:
        for curr in f:
            f, s = curr.strip().split(' ')
            l.append((f, int(s)))
    return l


if __name__ == '__main__':
    second()
