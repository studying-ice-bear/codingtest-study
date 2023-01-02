import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
nge = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack:
        if sequence[stack[-1]] < sequence[i]:
            nge[stack.pop()] = sequence[i]
        else:
            break
    stack.append(i)
        
print(*nge)
