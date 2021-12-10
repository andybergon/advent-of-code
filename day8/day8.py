from typing import List, Tuple

length_to_digit = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}
digit_to_length = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}
canonical_to_digit = {  # unused
    'abcefg': 0,  # 6
    'cf': 1,
    'acdeg': 2,  # 5
    'acdfg': 3,  # 5
    'bcdf': 4,
    'abdfg': 5,  # 5
    'abdefg': 6,  # 6
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,  # 6
}


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


def decode_trivial_maybe(e):
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


def deduce_row_value(e: Tuple[List]):
    signal_to_by_value = {}
    for signal in e[0]:
        if digit := decode_trivial_maybe(signal):
            populate_bimapping(signal_to_by_value, signal, digit)
        if len(signal_to_by_value) == 4 * 2:
            break
    # trivial: 1,4,7,8
    # 5 digits: 2,3,5
    # 6 digits: 0,6,9

    l_shape_set = set(signal_to_by_value[4]) - set(signal_to_by_value[1])

    for signal in e[0]:
        # 3 (need 1)
        if len(signal) == digit_to_length[3]:
            if signal_to_by_value[1].issubset(set(signal)):
                populate_bimapping(signal_to_by_value, signal, 3)
        # 5 (need 4)
        if len(signal) == digit_to_length[5]:
            if l_shape_set.issubset(set(signal)):
                populate_bimapping(signal_to_by_value, signal, 5)
        # 9 (need 1 and 7)
        if len(signal) == digit_to_length[9]:
            if set(signal_to_by_value[1]).issubset(set(signal)) and l_shape_set.issubset(set(signal)):
                populate_bimapping(signal_to_by_value, signal, 9)
        # 6 (need 1, exclude 0 and 9)
        if len(signal) == digit_to_length[6]:
            if not set(signal_to_by_value[1]).issubset(set(signal)):
                populate_bimapping(signal_to_by_value, signal, 6)

    for signal in e[0]:
        # 2 (need 3 and 5)
        if len(signal) == digit_to_length[2]:
            if signal_to_by_value.get(frozenset(signal)) is None:
                populate_bimapping(signal_to_by_value, signal, 2)
        # 0 (need 5, exclude 6 and 9)
        if len(signal) == digit_to_length[0]:
            if not set(signal_to_by_value[5]).issubset(set(signal)):
                populate_bimapping(signal_to_by_value, signal, 0)

    # print_line(e, signal_to_by_value)

    return calculate_value(e, signal_to_by_value)


def print_line(e, signal_to_by_value):
    for ee in e[0]:
        print(f'{signal_to_by_value[frozenset(ee)]} ', end='')
    print('- ', end='')
    for ee in e[1]:
        print(f'{signal_to_by_value[frozenset(ee)]} ', end='')
    print('')


def calculate_value(e, signal_to_by_value):
    value = 0
    for value_signal in e[1]:
        digit = signal_to_by_value[frozenset(value_signal)]
        value = value * 10 + digit
    return value


def populate_bimapping(signal_to_by_value, signal, digit):
    signal_set = frozenset(signal)
    signal_to_by_value[signal_set] = digit
    signal_to_by_value[digit] = signal_set


def sum_results(l):
    s = 0
    for row in l:
        value = deduce_row_value(row)
        s += value
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
part_two('day8.txt')  # ? # 1h (solving a different problem) + 1h
