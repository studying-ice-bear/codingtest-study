import sys
N = int(sys.stdin.readline())
ppl = list(map(int, sys.stdin.readline().split()))
ppl.sort()
times = [0] * N
times[0] = ppl[0]
total = times[0]
for i in range(1, N):
    times[i] = times[i - 1] + ppl[i]
    total += times[i]

print(total)
'''
문제 링크: https://www.acmicpc.net/problem/11399

'''