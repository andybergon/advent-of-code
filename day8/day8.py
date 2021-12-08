length_to_digit = {2: 1, 4: 4, 3: 7, 7: 8}
signal_to_digit = {
    'cagedb': 0,  # 6
    'ab': 1,
    'gcdfa': 2,  # 5
    'fbcad': 3,  # 5
    'eafb': 4,
    'cdfbe': 5,  # 5
    'cdfgeb': 6,  # 6
    'dab': 7,
    'acedgfb': 8,
    'cefabd': 9,  # 6
}
letter_set_to_digit = {frozenset(k): v for k, v in signal_to_digit.items()}


def load(filename):
    l = []
    with open(filename) as f:
        for r in f:
            notes, result = r.split('|')
            notes = [_ for _ in notes.strip().split()]
            result = [_ for _ in result.strip().split()]
            l.append((notes, result))
    return l


def is_easy(e):
    return len(e) in length_to_digit.keys()


def easy_to_digit_maybe(e):
    if is_easy(e):
        return length_to_digit[len(e)]
    return None


def count_easy_in_result(l):
    c = 0
    for row in l:
        for e in row[1]:
            if is_easy(e):
                c += 1
    return c


def sum_results(l):
    s = 0
    for row in l:
        num_str = ''
        for e in row[1]:
            easy_digit = easy_to_digit_maybe(e)
            if easy_digit:
                digit = easy_digit
            else:
                letter_set = frozenset(e)
                try:
                    digit = letter_set_to_digit[letter_set]
                except:
                    print(f'Not found {e}')
            num_str += str(digit)
        num = int(num_str)
        s = + num
    return s


def part_one(filename):
    l = load(filename)
    c = count_easy_in_result(l)
    print(c)


def part_two(filename):
    l = load(filename)
    s = sum_results(l)
    print(s)


# part_one('day8.txt')  # 387 # 10 min
part_two('day8test.txt')  # ? # 1h +
