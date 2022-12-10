def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def part_one(is_sample=False):
    l = open(get_filename(is_sample)).read().strip()
    print(l)


def part_two(is_sample=False):
    l = open(get_filename(is_sample)).read().strip()
    print(l)


if __name__ == "__main__":
    part_one(True)  # ? # ? mins
    # part_two(True)  # ? # ? mins
