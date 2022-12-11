import json
import math
from dataclasses import dataclass
from typing import Callable, List


def get_filename(is_sample=False, parsed=True):
    prefix = "parsed_" if parsed else ''
    return f"{prefix}input_sample.json" if is_sample else f"{prefix}input.json"


def parse_monkeys(is_sample=False):
    # TODO: do parsing instead of relying on parsed files
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


@dataclass
class Monkey:
    items: List[int]
    op_raw: str
    test_div: int
    true_i: int
    false_i: int

    @property
    def op(self) -> Callable[[int], int]:
        return eval(self.op_raw)


def get_monkeys(is_sample):
    monkeys = [Monkey(**m) for m in json.load(open(get_filename(is_sample)))]
    return monkeys


def print_end_round(monkeys):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {m["items"]}')


def calc_monkey_business(monkeys: List[Monkey], n_rounds, relief_f: Callable[[int], int]):
    inspections = [0 for _ in monkeys]
    for i_round in range(1, n_rounds + 1):
        for i, m in enumerate(monkeys):
            for worry_old in m.items:
                inspections[i] += 1
                worry = m.op(worry_old)
                worry = relief_f(worry)
                if worry % m.test_div:
                    target_i = m.false_i
                else:
                    target_i = m.true_i
                monkeys[target_i].items.append(worry)
            m.items = []
    monkey_business = math.prod(sorted(inspections, reverse=True)[:2])
    print(monkey_business)


def part_two(is_sample=False):
    monkeys = get_monkeys(is_sample)
    n_rounds = 10_000
    lcm_tests = math.lcm(*[m.test_div for m in monkeys])
    relief_f = lambda worry: worry % lcm_tests

    calc_monkey_business(monkeys, n_rounds, relief_f)


def part_one(is_sample=False):
    monkeys = get_monkeys(is_sample)
    n_rounds = 20
    relief_f = lambda worry: math.floor(worry / 3)

    calc_monkey_business(monkeys, n_rounds, relief_f)


if __name__ == "__main__":
    part_one(False)  # 108240 # 50 mins (20m parsing)
    part_two(False)  # 25712998901 # 30 mins (25m remember lcm (mcm in IT))
    # part 2 quite slower with @dataclass
