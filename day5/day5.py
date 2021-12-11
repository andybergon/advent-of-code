def load(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            splits = l.strip().split()
            x1, y1 = splits[0].split(',')
            x2, y2 = splits[2].split(',')
            lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return lines


def all_points_lines_1(lines):
    return [point for line in lines for point in all_points_1(*line)]


def all_points_lines_2(lines):
    return [point for line in lines for point in all_points_2(*line)]


def min_max(a, b):
    return min(a, b), max(a, b)


def all_points_1(p1, p2):
    points = []
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        mi, ma = min_max(y1, y2)  # check this is needed for range
        for i in range(mi, ma + 1):
            points.append((x1, i))
    elif y1 == y2:
        mi, ma = min_max(x1, x2)
        for i in range(mi, ma + 1):
            points.append((i, y1))
    else:
        pass
    return points


def is_45_degrees(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) == abs(y1 - y2)


def all_points_2(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if is_45_degrees(p1, p2):
        if x1 < x2 and y1 < y2:
            return to_up_right(p1, p2)
        elif x1 > x2 and y1 > y2:
            return to_up_right(p2, p1)
        elif x1 > x2 and y1 < y2:
            return to_down_right(p2, p1)
        else:
            return to_down_right(p1, p2)
    else:
        return all_points_1(p1, p2)


def to_up_right(p1, p2):
    points = []
    x1, y1 = p1
    x2, y2 = p2
    for i in range(x2 - x1 + 1):
        points.append((x1 + i, y1 + i))
    return points


def to_down_right(p1, p2):
    points = []
    x1, y1 = p1
    x2, y2 = p2
    for i in range(x2 - x1 + 1):
        points.append((x1 + i, y1 - i))
    return points


def get_maxs(points):
    max_x, max_y = 0, 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    return max_x, max_y


def get_grid(points):
    grid = initialize_grid(points)
    grid = update_grid(grid, points)
    return grid


def initialize_grid(points):
    grid = []
    max_x, max_y = get_maxs(points)  # could suppose constant
    for i in range(max_y):
        row = []
        for j in range(max_x):
            el = 0
            row.append(el)
        grid.append(row)
    return grid


def update_grid(grid, points):
    for point in points:
        x, y = point
        i, j = y - 1, x - 1
        grid[i][j] = grid[i][j] + 1
    return grid


def count_in_grid(grid, min=2):
    count = 0
    for r in grid:
        for e in r:
            if e >= min:
                count += 1
    return count


def part_one(filename='./day5.txt'):
    lines = load(filename)
    points = all_points_lines_1(lines)
    grid = get_grid(points)
    count = count_in_grid(grid)
    print(count)


def part_two(filename='./day5.txt'):
    lines = load(filename)
    points = all_points_lines_2(lines)
    grid = get_grid(points)
    count = count_in_grid(grid)
    print(count)


# part_one('./day5.txt')
part_two('./day5.txt')
