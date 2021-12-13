def load(filename):
    l = []
    with open(filename) as f:
        for row in f:
            l.append([a for a in row.strip()])
    return l


def part_one(filename):
    l = load(filename)
    print(l)


def part_two(filename):
    l = load(filename)
    print(l)


if __name__ == '__main__':
    part_one('day0test.txt')  # ? # ? min
    # part_two('day0test.txt')  # ? # ? min
