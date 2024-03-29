def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def part_one(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            l.append([a for a in row.strip()])
    print(l)


def part_two(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            l.append([a for a in row.strip()])
    print(l)


if __name__ == "__main__":
    part_one(True)  # ? # ? min
    # part_two(True)  # ? # ? min
