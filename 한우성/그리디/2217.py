import sys
input = sys.stdin.readline

n = int(input())

arr = sorted([int(input()) for i in range(n)], reverse=True)

answer = max([(arr[j]*(j+1)) for j in range(n)])

print(answer)