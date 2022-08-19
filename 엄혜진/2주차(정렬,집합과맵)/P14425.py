N, M = map(int, input().split())

S = {}
for _ in range(N):
    S[input()] = True

cases = []
for _ in range(M):
    cases.append(input())

answer = 0
for case in cases:
    if case in S:
        answer += 1

print(answer)