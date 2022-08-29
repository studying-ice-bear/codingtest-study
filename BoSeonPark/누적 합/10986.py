import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * m

temp = 0
for i in range(n):
    a[i] += temp
    temp = a[i]
    cnt[a[i] % m] += 1
    
ans = cnt[0]
for i in cnt:
    ans += (i * (i - 1)) // 2

print(ans)
