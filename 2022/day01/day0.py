with open('input.txt') as f:
    curr_cal = 0
    # could use priority queue
    top = [0, 0, 0]
    for line in f:
        v = line.strip()
        if len(v) == 0:
            i = min(top)
            if curr_cal > i:
                top[top.index(i)] = curr_cal
            curr_cal = 0
        else:
            curr_cal += int(v)

print(top)
print(sum(top))
