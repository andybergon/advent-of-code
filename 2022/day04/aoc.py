def fully_contained(range, test):
    low, high = range
    low_t, high_t = test
    if low <= low_t <= high and low <= high_t <= high:
        return True
    return False


def overlap(range, test):
    low, high = range
    low_t, high_t = test
    if low_t <= high and low <= high_t:
        return True
    return False


def part_one(is_sample=False):
    ranges = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            currs = []
            for pair in row.strip().split(","):
                l, r = pair.split("-")
                currs.append([int(l), int(r)])
            curr1, curr2 = currs
            if fully_contained(curr1, curr2) or fully_contained(curr2, curr1):
                ranges.append((curr1, curr2))
    print(len(ranges))


def part_two(is_sample=False):
    ranges = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            currs = []
            for pair in row.strip().split(","):
                l, r = pair.split("-")
                currs.append([int(l), int(r)])
            curr1, curr2 = currs
            if overlap(curr1, curr2) or overlap(curr2, curr1):
                ranges.append((curr1, curr2))
    print(len(ranges))


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


if __name__ == "__main__":
    part_one(False)  # 547 # 25 min (15 to figure out I was using strings)
    part_two(False)  # 843 # 15 min (was solving global overlaps)
