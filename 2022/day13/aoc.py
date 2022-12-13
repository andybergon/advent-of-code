import functools
import json


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def parse(s):
    return json.loads(s)


def correct_order(l, r, lvl=0, log=False):
    if log:
        print(f'{"  " * lvl}- Compare {l} vs {r}')
    l_int, r_int = type(l) == int, type(r) == int
    if l_int and r_int:
        if l == r:
            return 0
        else:
            correct = l < r
            if log:
                print(
                    f'{"  " * (lvl + 1)}- {"Left" if correct else "Right"} side is smaller, '
                    f'so inputs are{"" if correct else "NOT"} in the right order'
                )
            return 1 if correct else -1
    elif not l_int and not r_int:
        for i in range(max(len(l), len(r)) + 1):
            if len(l) <= i or len(r) <= i:
                if len(l) == len(r):
                    return 0
                else:
                    correct = len(l) <= i
                    if log:
                        print(
                            f'{"  " * (lvl + 1)}- {"Left" if correct else "Right"} side ran out of items,'
                            f' so inputs are {"" if correct else "NOT"} in the right order'
                        )
                    return 1 if correct else -1
            else:
                res = correct_order(l[i], r[i], lvl + 1, log)
                if res == 0:
                    continue
                else:
                    return res
    else:
        if log:
            print(
                f'{"  " * (lvl + 1)}- Mixed types; '
                f'convert {"left" if l_int else "right"} to {[l] if l_int else [r]} and retry comparison'
            )
        if l_int:
            return correct_order([l], r, lvl + 1, log)
        else:
            return correct_order(l, [r], lvl + 1, log)


def part_one(is_sample=False, log=False):
    pairs = open(get_filename(is_sample)).read().strip().split("\n\n")
    pairs = [tuple(pair.split("\n")) for pair in pairs]
    pairs = [(parse(t[0]), parse(t[1])) for t in pairs]

    in_order_idxs = []
    for i, (l, r) in enumerate(pairs):
        if log:
            print(f"== Pair {i + 1} ==")
        if correct_order(l, r, 0, log) == 1:
            in_order_idxs.append(i + 1)

    print(sum(in_order_idxs))


def part_two(is_sample=False):
    pairs = open(get_filename(is_sample)).read().strip().split("\n\n")
    packets = [parse(e) for pair in pairs for e in pair.split("\n")]
    div_start = [[2]]
    div_end = [[6]]
    packets = [*packets, div_start, div_end]
    packets = sorted(packets, key=functools.cmp_to_key(correct_order), reverse=True)

    # print('\n'.join(map(str, packets)))
    print((packets.index(div_start) + 1) * (packets.index(div_end) + 1))


if __name__ == "__main__":
    # start 05:42
    part_one(False, log=True)  # 5340 # 1h10m mins (06:53, +1 error for 20 mins)
    part_two(False)  # 21276 # 12 mins (07:05)
