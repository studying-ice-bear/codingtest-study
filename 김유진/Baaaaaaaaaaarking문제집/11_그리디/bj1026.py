import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)
total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)

'''
문제 링크: https://www.acmicpc.net/problem/1026
B의 배열에서 가장 작은 수에 A의 배열에서 가장 큰 수를 곱한다.
'''