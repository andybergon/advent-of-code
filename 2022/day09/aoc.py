def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


diffs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def needs_to_move(h, t):
    ih, jh = h
    it, jt = t
    if abs(ih-it) > 1 or abs(jh-jt) > 1:
        return True
    return False

def part_one(is_sample=False):
    # (i,j)
    h = prev_h = (0, 0)
    t = (0, 0)
    t_visited = {(0, 0)}
    l = open(get_filename(is_sample)).read().strip().split("\n")
    motions = [m.split(" ") for m in l]
    for direction, amt in motions:
        # todo: int(amt) in parsing
        for i in range(0, int(amt)):
            diff = diffs[direction]
            prev_h = h
            h = (h[0] + diff[0], h[1] + diff[1])
            if needs_to_move(h, t):
                t = prev_h
                t_visited.add(t)
    print(len(t_visited))


def part_two(is_sample=False):
    l = open(get_filename(is_sample)).read().strip()
    print(l)


if __name__ == "__main__":
    part_one(False)  # 6087 # 15 mins
    # part_two(True)  # ? # ? mins
