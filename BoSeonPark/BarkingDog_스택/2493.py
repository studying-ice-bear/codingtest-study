import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int, input().split()))
stack = []
reception = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            reception[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    
    if len(stack) == 0:
        reception[i] = 0
    
    stack.append([i, tower[i]])
    
    
print(*reception)