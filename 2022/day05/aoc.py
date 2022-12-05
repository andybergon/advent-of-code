def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def get_input(is_sample):
    with open(get_filename(is_sample)) as f:
        start, procedure = f.read().split("\n\n")
    start_splits = start.split("\n")
    n_cols = int(start_splits[-1][-1])
    curr_row = 1
    stacks = []
    for i in range(0, n_cols):
        stacks.append([])
    for j in range(1, len(start_splits)):
        i = 0
        row = start_splits[-1 - j].replace(" " * 5, " [.] ").replace("    [", "[.] [")

        curr_crates = row.split(" ")
        for crate in curr_crates:
            if crate == "[.]":
                i += 1
                continue
            stacks[i].append(crate.replace("[", "").replace("]", ""))
            i += 1
        curr_row += 1

    procedure = procedure.strip().split("\n")
    parsed_procedure = []
    for instr in procedure:
        import re

        m = re.match("move (\d+) from (\d+) to (\d+)", instr)
        parsed_procedure.append([int(v) for v in m.groups()])

    return stacks, parsed_procedure


def print_output(stacks):
    s = ""
    for c in stacks:
        s += c.pop()
    print(s)


def part_one(is_sample=False):
    stacks, procedure = get_input(is_sample)

    for p in procedure:
        c, fr, to = p
        for _ in range(0, c):
            stacks[to - 1].append(stacks[fr - 1].pop())

    print_output(stacks)


def part_two(is_sample=False):
    stacks, procedure = get_input(is_sample)

    for p in procedure:
        c, fr, to = p
        stack = stacks[fr - 1]
        to_move = stack[-c:]
        stacks[fr - 1] = stacks[fr - 1][:-c]
        stacks[to - 1].extend(to_move)

    print_output(stacks)


if __name__ == "__main__":
    part_one(False)  # SPFMVDTZT # 40 min (20 min parsing file)
    part_two(False)  # ZFSJBPRFP # 10 min
