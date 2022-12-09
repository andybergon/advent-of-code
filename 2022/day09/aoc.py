def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


diffs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def needs_to_move(h, t):
    ih, jh = h
    it, jt = t
    if abs(ih - it) > 1 or abs(jh - jt) > 1:
        return True
    return False


def part_one(is_sample=False):
    h = t = (0, 0)
    t_visited = {(0, 0)}
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    motions = [(d, int(amt)) for (d, amt) in [row.split(" ") for row in rows]]
    for direction, amt in motions:
        for i in range(0, amt):
            diff = diffs[direction]
            prev_h = h
            h = tuple(sum(comp) for comp in zip(h, diff))
            if needs_to_move(h, t):
                t = prev_h
                t_visited.add(t)
    print(len(t_visited))


def touching(n1, n2):
    return all([abs(c1 - c2) <= 1 for (c1, c2) in zip(n1, n2)])


def sign(n):
    return (n > 0) - (n < 0)


def move_adjecent(h, t):
    if h[0] == t[0]:
        return t[0], t[1] + sign(h[1] - t[1])
    elif h[1] == t[1]:
        return t[0] + sign(h[0] - t[0]), t[1]
    else:
        return t[0] + sign(h[0] - t[0]), t[1] + sign(h[1] - t[1])


def part_two(is_sample=False):
    part_two_generic(is_sample, 10)


def part_two_generic(is_sample, N):
    nodes = [(0, 0) for _ in range(N)]
    t_visited = {(0, 0)}
    l = open(get_filename(is_sample)).read().strip().split("\n")
    motions = [m.split(" ") for m in l]
    for direction, amt in motions:
        diff = diffs[direction]
        for _ in range(0, int(amt)):
            for i, v in enumerate(nodes):
                if i == 0:
                    new = tuple(sum(comp) for comp in zip(v, diff))
                    nodes[i] = new
                if i > 0 and not (touching(nodes[i - 1], nodes[i])):
                    nodes[i] = move_adjecent(nodes[i - 1], nodes[i])
                    if i == N - 1:
                        t_visited.add(nodes[i])
            # print_grid(nodes)
    print(len(t_visited))


def part_one_using_part_two(is_sample=False):
    part_two_generic(is_sample, 2)


def print_grid(nodes):
    pos_to_knots = {}
    for i, t in enumerate(nodes):
        pos_to_knots[t] = [*pos_to_knots.get(t, []), i]
    x, y = tuple(max(c) for c in zip(*nodes))
    x, y = x | 6, y | 5
    for i in range(y - 1, -1, -1):
        for j in range(0, x):
            knots = pos_to_knots.get((j, i), [])
            match len(knots):
                case 0:
                    to_print = '. '
                case 1:
                    to_print = f'{min(knots)} '
                case _:
                    to_print = f'{min(knots)}*'
            to_print = to_print.replace('0', 'H')
            print(to_print, end='')
        print()
    print('= ' * y)


if __name__ == "__main__":
    part_one(False)  # 6087 # 15 mins
    part_two(False)  # 2493 # 1h15m mins
    part_one_using_part_two(False)
