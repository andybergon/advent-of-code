def load(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            lines.append(l.strip())

    nums = lines[0]
    lines = lines[2:]

    boards = []
    curr_board = []
    for l in lines:
        if l == '':
            boards.append(curr_board)
            curr_board = []
        else:
            curr_board.append([int(e) for e in l.split()])
    boards.append(curr_board)

    nums = [int(e) for e in nums.split(',')]
    boards = [[[(el, False) for el in row] for row in board] for board in boards]

    print(nums)
    print(len(boards))
    return nums, boards


def mark_boards(boards, num):
    for board in boards:
        mark_board(board, num)


def mark_board(board, num):
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if el[0] == num:
                board[i][j] = (el[0], True)
                # return # if numbers can't be repeated in a board


def check_boards_1(boards):
    for i, board in enumerate(boards):
        if check_board(board):
            return i
    return None


def check_boards_2(boards):
    winning = []
    for i, board in enumerate(boards):
        if check_board(board):
            winning.append(i)
    return winning


def check_board(board):
    #  check rows
    for row in board:
        is_winning = True
        for el in row:
            is_winning = is_winning and el[1]
            if not is_winning:
                break
        if is_winning:
            return True

    # check columns
    matrix_dimension = len(board)
    for j in range(matrix_dimension):  # suppose constant and square matrices
        is_winning = True
        for i in range(matrix_dimension):
            is_winning = is_winning and board[i][j][1]
            if not is_winning:
                break
        if is_winning:
            return True


def calculate_score(board, last_num):
    # sum unmarked * last number called
    unmarked_sum = 0
    for row in board:
        for el in row:
            if not el[1]:
                unmarked_sum += el[0]
    return unmarked_sum * last_num


def part_one(filename='./day4.txt'):
    nums, boards = load(filename)
    for n in nums:
        mark_boards(boards, n)
        i = check_boards_1(boards)
        if i:
            print(f'Winning Board ({i}):\n{boards[i]}')
            score = calculate_score(boards[i], n)
            print(f'Score: {score} (Last Num: {n})')
            return score


def part_two(filename='./day4.txt'):
    nums, boards = load(filename)
    for n in nums:
        mark_boards(boards, n)
        winners = check_boards_2(boards)
        if winners and len(boards) > 1:
            boards = [b for i, b in enumerate(boards) if i not in winners]
            continue

        if winners and len(boards) == 1:
            print(f'Last Winning Board:\n{boards[0]}')
            score = calculate_score(boards[0], n)
            print(f'Score: {score} (Last Num: {n})')
            return

        if len(boards) == 0:
            print('No single winning board in last round!')
            return


# part_one()
part_two()
