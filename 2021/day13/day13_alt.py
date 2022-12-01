import numpy as np
from parse import findall

instr = open('day13.txt').read()
P = np.zeros((9999, 9999), bool)

for x, y in findall('{:d},{:d}', instr):
    P[y, x] = True

for axis, a in findall('{:l}={:d}', instr):
    if axis == 'x': P = P[:, :a] | P[:, 2 * a:a:-1]
    if axis == 'y': P = P[:a, :] | P[2 * a:a:-1, :]

print(np.array2string(P, separator='', formatter={'bool': {0: ' ', 1: '█'}.get}))
