import sys

n = int(sys.stdin.readline().rstrip())
top = list(map(int, sys.stdin.readline().split()))
temp = []
answer = [-1 for _ in range(n)]

for i in range(n - 1, -1, -1):
    if not temp or top[i] < top[temp[-1]]:
        temp.append(i)
    else:
        while temp and top[temp[-1]] < top[i]:
            answer[temp.pop()] = i + 1
        temp.append(i)

while temp:
    answer[temp.pop()] = 0

print(' '.join(map(str, answer)))
