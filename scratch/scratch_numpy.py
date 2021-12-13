import numpy as np


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            ch = '#' if m[i][j] else '.'
            print(ch, end='')
        print()


if __name__ == '__main__':
    m = [[False for _ in range(5)] for _ in range(8)]
    m[0][0] = True
    m[6][3] = True

    m_np = np.array(m)
    m_np_flip = np.flip(m_np, axis=0)

    np.split(m_np, )
    print_m(m_np)
