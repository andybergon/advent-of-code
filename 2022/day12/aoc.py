import collections
import math


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right


def find(grid, c):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == c:
                return i, j


def find_all(grid, c):
    l = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == c:
                l.append((i, j))
    return l


def elevation(v: str):
    v = v.replace("S", "a").replace("E", "z")
    return ord(v)


def get_visitables(grid, min_paths, curr):
    i, j = curr
    l = []
    for d in directions:
        di, dj = d
        ii = i + di
        jj = j + dj
        if (
            (0 <= ii < len(grid) and 0 <= jj < len(grid[0]))
            and min_paths[ii][jj] == math.inf
            and elevation(grid[ii][jj]) <= elevation(grid[i][j]) + 1
        ):
            l.append((ii, jj))
    return l


def calc_min_paths(grid, min_paths, q):
    while q:
        curr = q.popleft()
        visitables = get_visitables(grid, min_paths, curr)
        for visitable in visitables:
            q.append(visitable)
            ci, cj = curr
            vi, vj = visitable
            min_paths[vi][vj] = min_paths[ci][cj] + 1


def get_min_path(grid, start, end):
    min_paths = [[math.inf for _ in row] for row in grid]
    min_paths[start[0]][start[1]] = 0

    q = collections.deque()
    q.append(start)

    calc_min_paths(grid, min_paths, q)

    ei, ej = end
    return min_paths[ei][ej]


def part_one(is_sample=False):
    rows = open(get_filename(is_sample)).read().splitlines()
    grid = [[*row] for row in rows]
    curr = find(grid, "S")
    end = find(grid, "E")
    m = get_min_path(grid, curr, end)

    print(m)


def part_two(is_sample=False):
    rows = open(get_filename(is_sample)).read().splitlines()
    grid = [[*row] for row in rows]
    end = find(grid, "E")

    m = math.inf
    for curr in [*find_all(grid, "a"), find(grid, "S")]:
        m = min(m, get_min_path(grid, curr, end))
    print(m)


if __name__ == "__main__":
    part_one(False)  # 408 # 1h42m mins
    part_two(False)  # 399 # 10 mins
