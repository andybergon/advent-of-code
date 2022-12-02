column1_map = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
column2_map = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
column2_part2_map = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}  # me
shape_points = {'rock': 1, 'paper': 2, 'scissors': 3}
wins_over = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
loses_over = {v: k for k, v in wins_over.items()}


def part_one(is_sample=False):
    tot = 0
    with open(get_filename(is_sample)) as f:
        for row in f:
            oppo, me = row.split()
            oppo = column1_map[oppo]
            me = column2_map[me]
            tot += shape_points[me]
            if wins_over[me] == oppo:
                tot += 6
            elif wins_over[oppo] == me:
                tot += 0
            else:
                tot += 3
    print(tot)


def part_two(is_sample=False):
    tot = 0
    with open(get_filename(is_sample)) as f:
        for row in f:
            oppo, result = row.split()
            oppo = column1_map[oppo]
            result = column2_part2_map[result]
            me = get_move(oppo, result)
            tot += shape_points[me]
            if wins_over[me] == oppo:
                tot += 6
            elif wins_over[oppo] == me:
                tot += 0
            else:
                tot += 3
    print(tot)


def get_move(other_move, result):
    if result == 'draw':
        return other_move
    elif result == 'win':
        return loses_over[other_move]
    else:
        return wins_over[other_move]


def get_filename(is_sample=False):
    return 'input_sample.txt' if is_sample else 'input.txt'


if __name__ == '__main__':
    part_one(False)  # ? # 15 min
    # part_two(True)  # ? # 5 min
