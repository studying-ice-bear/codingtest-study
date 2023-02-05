import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0


def backtracking(current, total):
    global cnt
    if current == N:
        if total == S:
            cnt += 1
        return
    backtracking(current + 1, total)
    backtracking(current + 1, total + arr[current])


backtracking(0, 0)

if S == 0:
    cnt -= 1

print(cnt)

'''
문제 링크: https://www.acmicpc.net/problem/1182
5 0
-7 -3 -2 5 8
'''