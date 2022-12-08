from math import prod


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def is_visible(h, vis, ij):
    i, j = ij
    if vis[ij]:
        return True
    if i == 0 or j == 0 or i == len(h) or j == len(h[j]):
        vis[ij] = True
        return True
    # return is_visible_from(h, ij, )
    return False


def part_one_old(is_sample=False):
    h = [[*row] for row in open(get_filename(is_sample)).read().strip().split("\n")]
    c = 0
    vis = {}  # {(i,j): True}
    for j in range(0, len(h)):
        for i in range(0, len(h[j])):
            c += is_visible(h, vis, (i, j))
    print(c)
    # obs: would make sense to iterate per "circular layer"


def visible_in_seq(seq):
    indicies = [0]
    for i in range(1, len(seq)):
        if seq[i - 1] < seq[i]:
            indicies.append(i)
    return indicies

    # indicies = visible_in_seq(seq)
    # for idx in indicies:
    #     j = idx if left_to_right else len(seq) - idx - 1
    #     vis[(i, j)] = True


# def visible_in_column(h, vis, j, up_to_down):
#     seq = []
#     vis[()]
#     for i in range(1, len(h)):
#         seq.append(h[i][j])
#     indicies = visible_in_seq(seq)
#     for idx in indicies:
#         i = idx if up_to_down else len(h[0]) - idx - 1
#         vis[(i, j)] = True


# def print_matrix(h, vis):
#     for i in range(0, n):
#         for j in range(0,m):
#             print(f'{vis.get((i,j), " ")}', end='')
#         print()


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

    # print_matrix(h, vis)
    print(vis)
    print(len(vis))


def score(h, ij):
    i_house, j_house = ij
    h_house = h[i_house][j_house]
    dir_s = []

    s = 0
    for i in range(i_house - 1, -1, -1):  # UP
        if h[i][j_house] < h_house:
            s += 1
        elif h[i][j_house] >= h_house:
            s += 1
            break
    dir_s.append(s)

    s = 0
    for i in range(i_house + 1, len(h)):  # DOWN
        if h[i][j_house] < h_house:
            s += 1
        elif h[i][j_house] >= h_house:
            s += 1
            break
    dir_s.append(s)

    s = 0
    for j in range(j_house + 1, len(h[0])):  # RIGHT
        if h[i_house][j] < h_house:
            s += 1
        elif h[i_house][j] >= h_house:
            s += 1
            break
    dir_s.append(s)

    s = 0
    for j in range(j_house - 1, -1, -1):  # LEFT
        if h[i_house][j] < h_house:
            s += 1
        elif h[i_house][j] >= h_house:
            s += 1
            break
    dir_s.append(s)

    return prod(dir_s)


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
