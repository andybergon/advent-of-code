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


def get_filename(is_sample=False):
    return 'input_sample.txt' if is_sample else 'input.txt'


if __name__ == '__main__':
    part_one(True)  # ? # ? min
    # part_two(True)  # ? # ? min
