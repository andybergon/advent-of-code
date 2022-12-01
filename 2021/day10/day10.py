err_par_to_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
opening = '([{<'
closing = ')]}>'
relative = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
compl_par_to_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def load(filename):
    l = []
    with open(filename) as f:
        for row in f:
            l.append(row.strip())
    return l


def is_corrupted(line):
    stack = []
    for ch in line:
        if ch in opening:
            stack.append(ch)
        else:
            last_o = stack.pop()
            if relative[last_o] != ch:
                return err_par_to_score[ch]
    return 0


def calc_score(line):
    stack = []
    for ch in line:
        if ch in opening:
            stack.append(ch)
        else:
            last_o = stack.pop()
            if relative[last_o] != ch:
                raise ValueError('Use this only on NOT corrupted lines!')

    closing = [relative[stack.pop()] for _ in range(len(stack))]
    return score_from_closing(closing)


def score_from_closing(closing):
    score = 0
    for c in closing:
        score = score * 5 + compl_par_to_score[c]
    return score


def median_score(scores):
    return sorted(scores)[len(scores) // 2]


def part_one(filename):
    l = load(filename)
    s = sum(map(is_corrupted, l))
    print(s)


def part_two(filename):
    l = load(filename)
    l = list(filter(lambda x: not (is_corrupted(x)), l))
    scores = [calc_score(line) for line in l]
    s = median_score(scores)
    print(s)


# part_one('day10.txt')  # 390993 # 25 min
part_two('day10.txt')  # 2391385187 # 20 min
