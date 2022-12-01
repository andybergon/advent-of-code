import heapq

TOP_SIZE = 3

q = []
with open('input.txt') as f:
    curr_cal = 0
    for line in f:
        v = line.strip()
        if len(v) == 0:
            # alt: PriorityQueue
            if len(q) < TOP_SIZE:
                heapq.heappush(q, curr_cal)
            else:
                heapq.heappushpop(q, curr_cal)
            curr_cal = 0
        else:
            curr_cal += int(v)

print(q)
print(sum(q))
