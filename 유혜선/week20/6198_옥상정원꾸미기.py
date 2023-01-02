import sys

input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]
INF = int(10e9)
buildings.append(INF)
answer = [0] * n
stack = []

for idx, val in enumerate(buildings):
    while stack:
        if stack[-1][0] <= val:
            val_p, idx_p = stack.pop()
            diff = idx - idx_p - 1
            answer[idx_p] = diff
        else:
            break
    
    stack.append((val, idx))


print(sum(answer))