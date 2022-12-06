import queue

def get_filename(is_sample=False):
    return "input_sample.txt" if is_sample else "input.txt"

N = 14
M = N-1
# 4 diff chars, most recent, num from beginning to end of 4
def part_one(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        seq = f.read().strip()
        for i in range(M, len(seq)):
            sub = seq[i-M:i+1]
            if len(set(sub)) == N:
                print(i+1)
                return

        print(seq)


def part_two(is_sample=False):
    l = []
    with open(get_filename(is_sample)) as f:
        for row in f:
            l.append([a for a in row.strip()])
    print(l)


if __name__ == "__main__":
    part_one(False)  # ? # ? min
    # part_two(True)  # ? # ? min
