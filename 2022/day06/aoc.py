def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def find_start(is_sample=False, n=4):
    m = n - 1
    with open(get_filename(is_sample)) as f:
        seq = f.read().strip()
    for i in range(m, len(seq)):
        sub = seq[i - m : i + 1]
        if len(set(sub)) == n:
            print(i + 1)
            return
    print(seq)


def part_one(is_sample=False):
    find_start(is_sample, 4)


def part_two(is_sample=False):
    find_start(is_sample, 14)


if __name__ == "__main__":
    part_one(False)  # 1034 # 6 min
    part_two(False)  # 2472 # 1 min
