import sys

n = int(sys.stdin.readline())
answer = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        answer.pop()
    else:
        answer.append(num)

print(sum(answer))