import re


def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"


def is_valid_one(passwd, mi, ma, ch):
    chs = {}
    for c in passwd:
        chs[c] = chs.get(c, 0) + 1
    ch_count = chs.get(ch, 0)
    return mi <= ch_count <= ma

def is_valid_two(passwd, pos1, pos2, ch):
    return (passwd[pos1 -1] == ch) ^ (passwd[pos2 -1] == ch)


def part_one(is_sample=False):
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    count = 0
    for row in rows:
        policy, passwd = row.split(": ")
        mi, ma, ch = re.match(r"(\d+)-(\d+) (\b[a-z])", policy).groups()
        mi, ma = int(mi), int(ma)
        count += is_valid_one(passwd, mi, ma, ch)
    print(count)


def part_two(is_sample=False):
    rows = open(get_filename(is_sample)).read().strip().split("\n")
    count = 0
    for row in rows:
        policy, passwd = row.split(": ")
        pos1, pos2, ch = re.match(r"(\d+)-(\d+) (\b[a-z])", policy).groups()
        pos1, pos2 = int(pos1), int(pos2)
        count += is_valid_two(passwd, pos1, pos2, ch)
    print(count)


if __name__ == "__main__":
    # part_one(False)  # ? # 20 mins
    part_two(False)  # ? # 4 min
