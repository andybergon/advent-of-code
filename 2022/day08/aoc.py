from math import prod


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def mark_visible_in_row(h, vis, i):
    seq = h[i]
    biggest_so_far = -1

    for j in range(0, len(seq)):
        v = int(seq[j])
        if biggest_so_far < v:
            vis[(i, j)] = True
        biggest_so_far = max(v, biggest_so_far)

    biggest_so_far = -1
    for j in range(len(seq) - 1, -1, -1):
        v = int(seq[j])
        if biggest_so_far < v:
            vis[(i, j)] = True
        biggest_so_far = max(v, biggest_so_far)


def visible_in_column(h, vis, j):
    biggest_so_far = -1
    for i in range(0, len(h)):
        v = int(h[i][j])
        if biggest_so_far < v:
            vis[(i, j)] = True
        biggest_so_far = max(v, biggest_so_far)

    biggest_so_far = -1
    for i in range(len(h) - 1, -1, -1):
        v = int(h[i][j])
        if biggest_so_far < v:
            vis[(i, j)] = True
        biggest_so_far = max(v, biggest_so_far)


def part_one(is_sample=False):
    h = [[*row] for row in open(get_filename(is_sample)).read().strip().split("\n")]
    vis = {}  # {(i,j): True}
    for i in range(0, len(h)):
        mark_visible_in_row(h, vis, i)
    for j in range(0, len(h[0])):
        visible_in_column(h, vis, j)
    print(len(vis))


def score_single(h, ij, ascending, i_over_j):
    i_house, j_house = ij
    h_house = h[i_house][j_house]
    s = 0

    step = 1 if ascending else -1
    start = (i_house if i_over_j else j_house) + (step)
    end = -1 if not ascending else (len(h) if i_over_j else len(h[0]))
    for x in range(start, end, step):
        v = h[x][j_house] if i_over_j else h[i_house][x]
        if v < h_house:
            s += 1
        elif v >= h_house:
            s += 1
            break
    return s


def score(h, ij):
    # up, left, down, right
    dirs = [(0, 1), (0, 0), (1, 1), (1, 0)]
    return prod([score_single(h, ij, t[0], t[1]) for t in dirs])


def part_two(is_sample=False):
    h = [[*row] for row in open(get_filename(is_sample)).read().strip().split("\n")]
    scores = []
    # discarding outer ring from start, avoids conditions on edges later
    for i in range(1, len(h) - 1):
        for j in range(1, len(h[0]) - 1):
            scores.append(score(h, (i, j)))
    print(max(scores))


if __name__ == "__main__":
    part_one(False)  # 1684 # 68 mins
    part_two(False)  # 486540 # 31 mins
