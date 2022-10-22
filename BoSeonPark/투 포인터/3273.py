import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
l, r = 0, n - 1
answer = 0

while l != r:
    if a[l] + a[r] == x:
        answer += 1
        r -= 1
    elif a[l] + a[r] < x:
        l += 1
    elif a[l] + a[r] > x:
        r -= 1

print(answer)