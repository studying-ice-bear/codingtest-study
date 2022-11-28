import sys

T = int(sys.stdin.readline().rstrip())
m0 = [0] * 41
m1 = [0] * 41
m0[0], m0[1], m0[2] = 1, 0, 1
m0_idx = 2
m1[0], m1[1], m1[2] = 0, 1, 1
m1_idx = 2
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    if m0_idx < n:
        for k in range(m0_idx, n + 1):
            m0[k] = m0[k - 1] + m0[k - 2]
        m0_idx = n

    if m1_idx < n:
        for k in range(m1_idx, n + 1):
            m1[k] = m1[k - 1] + m1[k - 2]
        m1_idx = n

    print(m0[n], m1[n])

