import re


def part_one(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        start, procedure = f.read().split("\n\n")
        start_splits = start.split('\n')
        n_cols = int(start_splits[-1][-1])
        curr_row = 1
        stacks = []
        for i in range(0, n_cols):
            stacks.append([])
        for j in range(1, len(start_splits)):
            i = 0
            row = start_splits[-1 - j]
            row = row.replace(' ' * 5, ' [.] ')
            row = row.replace('    [', '[.] [')
            curr_crates = row.split(' ')
            for crate in curr_crates:
                if crate == '[.]':
                    i += 1
                    continue
                stacks[i].append(crate.replace('[', '').replace(']', ''))
                i += 1
            curr_row += 1

        procedure = procedure.strip().split('\n')
        parsed_procedure = []
        for instr in procedure:
            import re
            m = re.match('move (\d+) from (\d+) to (\d+)', instr)
            parsed_procedure.append([int(v) for v in m.groups()])

        print(stacks)
        print(parsed_procedure)

        # for p in parsed_procedure:
        #     c, fr, to = p
        #     for _ in range(0, c):
        #         stacks[to-1].append(stacks[fr-1].pop())
        # print(stacks)
        for p in parsed_procedure:
            c, fr, to = p
            stack = stacks[fr-1]
            to_move = stack[-c:]
            stacks[fr-1] = stacks[fr-1][:-c]
            stacks[to-1].extend(to_move)
        print(stacks)

        s = ''
        for c in stacks:
            s+= c.pop()
        print(s)


def part_two(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            l.append([a for a in row.strip()])
    print(l)


def get_filename(is_sample=False):
    return 'input_sample.txt' if is_sample else 'input.txt'


if __name__ == '__main__':
    part_one(False)  # ? # 40 min (20 min parsing)
    # part_two(True)  # ? # 10 min
