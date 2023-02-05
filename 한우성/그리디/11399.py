import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
answer = 0
P.sort()

for i in range(1, N+1):
    answer += sum(P[0:i])

print(answer)