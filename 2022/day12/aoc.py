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
            and min_paths[ii][jj] == -math.inf
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


def part_one(is_sample=False):
    # check .splitlines()
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    grid = [[*row] for row in rows]
    curr = find(grid, "S")
    end = find(grid, "E")
    min_paths = [[-math.inf for _ in row] for row in rows]
    min_paths[curr[0]][curr[1]] = 0
    q = collections.deque()
    q.append(curr)

    calc_min_paths(grid, min_paths, q)

    ei, ej = end
    print(min_paths[ei][ej])


def part_two(is_sample=False):
    l = open(get_filename(is_sample)).read().strip()
    print(l)


if __name__ == "__main__":
    # part_one(False)  # 408 # 1h42m mins
    part_two(True)  # ? # ? mins
