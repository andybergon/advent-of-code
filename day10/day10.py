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


part_one('day10test.txt')  # ? # ? min
# part_two('day10test.txt')  # ? # ? min
