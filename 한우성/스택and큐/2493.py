import sys

input = sys.stdin.readline
n = int(input())
signal = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    send = signal[i]
    while stack:
        if send < stack[-1][1]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            answer[i] = 0
            stack.pop()
    stack.append([i, send])

print(*answer)
        

