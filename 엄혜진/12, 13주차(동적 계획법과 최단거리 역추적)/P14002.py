import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
# print(n, a)

# 30840KB	196ms
dp = [0 for _ in range(n + 1)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

sub_a = []
max_cnt = max(dp)
idx = dp.index(max_cnt)

for i in range(idx, -1, -1):
    if max_cnt == dp[i]:
        sub_a.append(a[i])
        max_cnt -= 1
print(len(sub_a))
sub_a.reverse()
print(' '.join(map(str, sub_a)))

# 11053번 문제를 완전 잊고 있었다
