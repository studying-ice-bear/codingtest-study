
'''
1 1 1 2 2 3 4 5 7 9

P(0) = 0
P(1) = 1
P(2) = P(0) + P(1) = 1
P(3) = P(0) + P(2) = 1
P(4) = P(1) + P(3) = 2
P(5) = P(2) + P(3) = 2

P(6) = P(3) + P(4) = 3
P(7) = P(4) + P(5) = 4
P(8) = P(5) + P(6) = 5
P(9) = P(6) + P(7) = 7
P(10) = P(7) + P(8) = 9
'''

import sys
T = int(sys.stdin.readline())

''' 재귀함수 시간초과
def P(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return P(n-3) + P(n-2)
'''


for _ in range(T):
    N = int(sys.stdin.readline())
    memory = [0] * (N+1)

    for i in range(N+1):
        if i == 0:
            memory[i] = 0
        elif i == 1:
            memory[i] = 1
        elif i == 2:
            memory[i] = 1
        else:
            memory[i] = memory[i-3] + memory[i-2]
    print(memory[N])
