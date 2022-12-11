import json
import math


def get_filename(is_sample=False, parsed=True):
    prefix = "parsed_" if parsed else ''
    return f"{prefix}input_sample.json" if is_sample else f"{prefix}input.json"


def parse_monkeys(is_sample=False):
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    monkeys = []
    for r in rows:
        match r:
            case ['Monkey ', i, ':']:
                monkey = {}
            case ['  Starting items: ', l]:
                start_items = [int(n.strip()) for n in l.split(',')]
                monkey['start'] = start_items
            case ['  Operation: ', op]:
                # parse manually
                # monkey['op'] = op
                monkey['op'] = lambda old: old + 0
            case ['  Test: divisible by ', n]:
                monkey['divisible'] = n
            case ['    If true: throw to monkey ', n]:
                monkey['true'] = n
            case ['    If false: throw to monkey ', n]:
                monkey['false'] = n
            case _:
                monkeys.append(monkey)
    print(monkeys)


def get_monkeys(is_sample):
    # items, op, test_div, true_i, false_i
    monkeys = json.load(open(get_filename(is_sample)))
    for m in monkeys:
        m['op'] = eval(m['op'])
    return monkeys


def print_end_round(monkeys):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {m["items"]}')


def part_one(is_sample=False):
    n_rounds = 20
    relief_factor = 3
    monkeys = get_monkeys(is_sample)

    inspections = [0 for _ in monkeys]

    for i_round in range(1, n_rounds + 1):
        for i, m in enumerate(monkeys):
            for worry_old in m['items']:
                # for i in [1,2,3].pop() - works?
                inspections[i] = inspections[i] + 1
                worry = m['op'](worry_old)
                worry = math.floor(worry / relief_factor)
                rem = worry % m['test_div']
                if rem:
                    target_i = m['false_i']

                else:
                    target_i = m['true_i']
                monkeys[target_i]['items'].append(worry)
            m['items'] = []
    monkey_business = math.prod(sorted(inspections, reverse=True)[:2])
    print(monkey_business)


def part_two(is_sample=False):
    n_rounds = 10_000
    relief_factor = 1
    monkeys = get_monkeys(is_sample)
    div_tests = set()
    for m in monkeys:
        div_tests.add(m['test_div'])
    lcm_tests = math.lcm(*div_tests)

    inspections = [0 for _ in monkeys]

    for i_round in range(1, n_rounds + 1):
        for i, m in enumerate(monkeys):
            for worry_old in m['items']:
                # for i in [1,2,3].pop() - works?
                # rename worry_new/after
                inspections[i] = inspections[i] + 1
                worry = m['op'](worry_old)
                worry = worry % lcm_tests
                rem = worry % m['test_div']
                if rem:
                    target_i = m['false_i']

                else:
                    target_i = m['true_i']
                monkeys[target_i]['items'].append(worry)
            m['items'] = []
    monkey_business = math.prod(sorted(inspections, reverse=True)[:2])
    print(monkey_business)


if __name__ == "__main__":
    part_one(False)  # 108240 # 50 mins (20m parsing)
    part_two(False)  # 25712998901 # 30 mins (25m remember mcm)
