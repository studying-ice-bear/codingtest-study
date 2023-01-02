import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for a, b in zip(A, B):
    answer += a * b

print(answer)