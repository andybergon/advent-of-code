from collections import defaultdict


def load(filename):
    edges = []
    with open(filename) as f:
        for row in f:
            edges.append(tuple(row.strip().split('-')))
    return edges


def add_or_append(d, k, v):  # built in multimap?
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]


def get_nexts(e):
    nexts = defaultdict(list)  # list for reproducibility sorting
    for a, b in e:
        # could manage start/end just as lower case visitable once
        if a != 'end' and b != 'start':
            nexts[a].append(b)
        if b != 'end' and a != 'start':
            nexts[b].append(a)
    return nexts


def count_paths(nexts):
    c = 0
    for next in nexts['start']:
        # curr_path for debugging
        c += count_paths_rec(next, nexts, set(), ['start', next])
    return c


def count_paths_rec(curr, nexts, small_visited, curr_path):
    if curr == 'end':
        print(curr_path)
        return 1

    if curr.islower():
        small_visited.add(curr)

    c = 0
    for next in nexts[curr]:
        if next.islower():
            if next not in small_visited:
                c += count_paths_rec(next, nexts, {*small_visited, next}, [*curr_path, next])
            else:
                continue
        else:
            c += count_paths_rec(next, nexts, {*small_visited}, [*curr_path, next])
    return c


def part_one(filename):
    e = load(filename)
    n = get_nexts(e)
    c = count_paths(n)
    print(c)


def part_two(filename):
    e = load(filename)
    print(e)


# part_one('day12.txt')  # 4011 (10/19/226) # 1h?
part_two('day12test.txt')  # # ? min
