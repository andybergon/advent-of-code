import functools
import json


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def parse(s):
    return json.loads(s)


def correct_order(l, r, lvl=0):
    print(f'{"  " * lvl}- Compare {l} vs {r}')
    l_int, r_int = type(l) == int, type(r) == int
    if l_int and r_int:
        if l == r:
            return 0
        elif l < r:
            print(f'{"  " * (lvl + 1)}- Left side is smaller, right order')
            return 1
        else:
            print(f'{"  " * (lvl + 1)}- Right side is smaller, NOT right order')
            return -1
    elif not l_int and not r_int:
        ii = max(len(l), len(r)) + 1
        for i in range(ii):
            if len(l) <= i or len(r) <= i:
                if len(l) == len(r):
                    return 0
                elif len(l) <= i:
                    print(
                        f'{"  " * (lvl + 1)}- Left side ran out of items, so inputs are in the right order'
                    )
                    return 1
                else:
                    print(
                        f'{"  " * (lvl + 1)}- Left side ran out of items, so inputs are NOT in the right order'
                    )
                    return -1
            else:
                res = correct_order(l[i], r[i], lvl + 1)
                if res == 0:
                    continue
                else:
                    return res
    else:
        if l_int:
            print(f'{"  " * (lvl + 1)}- Mixed types; convert left to {[l]} and retry comparison')
            return correct_order([l], r, lvl + 1)
        else:
            print(f'{"  " * (lvl + 1)}- Mixed types; convert right to {[r]} and retry comparison')
            return correct_order(l, [r], lvl + 1)


def part_one(is_sample=False):
    pairs = open(get_filename(is_sample)).read().strip().split("\n\n")
    pairs = [tuple(pair.split("\n")) for pair in pairs]
    pairs = [(parse(t[0]), parse(t[1])) for t in pairs]

    in_order_idxs = []
    for i, (l, r) in enumerate(pairs):
        print(f"== Pair {i + 1} ==")
        if correct_order(l, r, 0) == 1:
            in_order_idxs.append(i + 1)

    print(in_order_idxs)
    print(sum(in_order_idxs))


def part_two(is_sample=False):
    pairs = open(get_filename(is_sample)).read().strip().split("\n\n")
    packets = [parse(e) for pair in pairs for e in pair.split("\n")]
    div_start = [[2]]
    div_end = [[6]]
    packets = [*packets, div_start, div_end]
    # packets = sorted(packets)
    print(packets)
    packets = sorted(packets, key=functools.cmp_to_key(correct_order), reverse=True)
    for p in packets:
        print(p)

    print((packets.index(div_start) + 1) * (packets.index(div_end) + 1))
    # print('\n'.join(packets))


if __name__ == "__main__":
    # start 05:42
    # part_one(False)  # 5340 # 1h10m mins (06:53, +1 error for 20 mins)
    part_two(False)  # 21276 # 12 mins (07:05)
