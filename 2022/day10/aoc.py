def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def get_instructions(is_sample):
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    instructions = []
    for r in rows:
        match r.split(' '):
            case ['addx', n]:
                instructions.append((int(n), 2))
            case _:
                instructions.append((0, 1))
    return instructions


def part_one(is_sample=False):
    instructions = get_instructions(is_sample)

    x = 1
    cycle_i = 0
    cycles_to_sum = [20 + 40 * n for n in range(0, 6)]
    s = 0
    for instr in instructions:
        amt, cycles = instr
        for _ in range(cycles):
            cycle_i += 1
            if cycle_i in cycles_to_sum:
                signal_strength = x * cycle_i
                s += signal_strength
        x += amt
    print(s)


def part_two(is_sample=False):
    instructions = get_instructions(is_sample)

    x = 1
    cycle_i = 0
    pixel_i = -1
    for instr in instructions:
        amt, cycles = instr
        for _ in range(cycles):
            cycle_i += 1
            pixel_i += 1
            to_print = '#' if pixel_i in range(x - 1, x + 2) else '.'
            print(to_print, end='')
            if pixel_i == 39:
                print()
                pixel_i = -1
        x += amt


if __name__ == "__main__":
    part_one(False)  # 16480 # 40 mins (solved the wrong problem initially)
    part_two(False)  # ? # 15 mins
