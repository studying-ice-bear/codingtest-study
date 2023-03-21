import sys, math
N = int(sys.stdin.readline())
lines = []

for _ in range(N):
    lines.append(list(map(int, sys.stdin.readline().split())))

lines.sort()
left = lines[0][0]
right = lines[0][1]

answer = 0
for i in range(1, N):
    if right >= lines[i][1]:
        continue

    elif lines[i][0] <= right < lines[i][1]:
        right = lines[i][1]

    elif right < lines[i][0]:
        answer += right - left
        left = lines[i][0]
        right = lines[i][1]

answer += right - left
print(answer)
