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


def get_visitables(grid, visited, curr):
    i, j = curr
    l = []
    for d in directions:
        di, dj = d
        ii = i + di
        jj = j + dj
        new_curr = (ii, jj)
        if new_curr in visited:
            continue
        if not (0 <= ii < len(grid) and 0 <= jj < len(grid[0])):
            continue
        if elevation(grid[ii][jj]) <= elevation(grid[i][j]) + 1:
            l.append(new_curr)
    return l


def step(grid, min_paths, visited, path, curr, end):
    print(path)
    if curr == end:
        return path
    else:
        paths = []
        visitables = get_visitables(grid, visited, curr)
        for visitable in visitables:
            best_to_end = min_paths[curr[0]][curr[1]]
            if best_to_end < len(new_path):

            new_path = step(grid, min_paths, {*visited, visitable}, [*path, visitable], visitable, end)
            if new_path:
                paths.append(new_path)
        if paths:
            return min(paths, key=len)
        else:
            return None


def part_one(is_sample=False):
    # check .splitlines()
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    grid = [[*row] for row in rows]
    curr = find(grid, "S")
    end = find(grid, "E")
    visited = {curr}
    min_paths = [-math.inf for row in rows for _ in row]
    path = [curr]

    min_path = step(grid, min_paths, visited, path, curr, end)
    print(len(min_path))


def part_two(is_sample=False):
    l = open(get_filename(is_sample)).read().strip()
    print(l)


if __name__ == "__main__":
    part_one(False)  # ? # ? mins
    # part_two(True)  # ? # ? mins
