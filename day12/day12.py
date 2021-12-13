from collections import Counter, defaultdict


def load(filename):
    edges = []
    with open(filename) as f:
        for row in f:
            edges.append(tuple(row.strip().split('-')))
    return edges


def get_nexts(e):
    nexts = defaultdict(list)  # list for reproducibility sorting
    for a, b in e:
        # could manage start/end just as lower case visitable once
        if a != 'end' and b != 'start':
            nexts[a].append(b)
        if b != 'end' and a != 'start':
            nexts[b].append(a)
    return nexts


def count_paths(nexts, max_small=1):
    c = 0
    for next in nexts['start']:
        counter = Counter([next]) if next.islower() and next != 'end' else Counter()
        c += count_paths_rec(next, nexts, counter, ['start', next], max_small)
    return c


def can_visit_small(next, small_visited: Counter, max_small):
    most_common = small_visited.most_common(1)
    if most_common:
        most_common = most_common[0][1]
        if most_common == max_small:
            return small_visited[next] < 1
        else:
            return True
    return True


def count_paths_rec(curr, nexts, small_visited: Counter, curr_path, max_small):
    # curr_path for debugging only
    if curr == 'end':
        print(curr_path)
        return 1

    c = 0
    for next in nexts[curr]:
        if next.islower():
            if can_visit_small(next, small_visited, max_small):
                counter = Counter(small_visited)
                counter.update([next])
                c += count_paths_rec(next, nexts, counter, [*curr_path, next], max_small)
        else:
            c += count_paths_rec(next, nexts, Counter(small_visited), [*curr_path, next], max_small)
    return c


def part_one(filename):
    e = load(filename)
    n = get_nexts(e)
    c = count_paths(n)
    print(c)


def part_two(filename):
    e = load(filename)
    n = get_nexts(e)
    c = count_paths(n, 2)
    print(c)


# part_one('day12.txt')  # 4011 (10/19/226) # 1h?
part_two('day12.txt')  # 108035 # 1h? (bug: Counter('foo') != Counter(['foo']), first one uses single chars)
