def fully_contained(range, test):
    low, high = [int(x) for x in range.split('-')]
    low_t, high_t = [int(x) for x in test.split('-')]
    if low <= low_t <= high and low <= high_t <= high:
        return True
    return False

def overlap(range, test):
    low, high = [int(x) for x in range.split('-')]
    low_t, high_t = [int(x) for x in test.split('-')]
    if low_t <= high and low <= high_t:
        return True
    return False


def part_one(is_sample=False):
    ranges = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            curr1, curr2 = row.strip().split(',')
            if fully_contained(curr1, curr2) or fully_contained(curr2, curr1):
                ranges.append((curr1, curr2))
    print(len(ranges))


def part_two(is_sample=False):
    ranges = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            curr1, curr2 = row.strip().split(',')
            overlaps = overlap(curr1, curr2) or overlap(curr2, curr1)
            if overlaps:
                ranges.append((curr1, curr2))
    print(len(ranges))


def get_filename(is_sample=False):
    return 'input_sample.txt' if is_sample else 'input.txt'


if __name__ == '__main__':
    part_one(False)  # ? # 25 min (15 to figure out I was using strings)
    part_two(False)  # ? # 15 min (was solving gobal overlaps)
