import sys
input = sys.stdin.readline

answer = 0
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(N):
    answer += A.pop(0) * B.pop(0)

print(answer)