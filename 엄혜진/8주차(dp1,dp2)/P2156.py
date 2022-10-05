import sys

n = int(sys.stdin.readline().rstrip())

wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline().rstrip()))
# print(wine)

dp = [0] * n

# 도저히 모르겠어서 블로그 참조
# 3잔을 연달아 마실 수 없기 때문에 최대로 많이 마시는 경우의 수는 총 3가지가 있다.
# 1. N은 안 마시고 N-1 까지 최대로 마시기 [..., X]
# 2. N은 마시고 N-1은 안 마시고 N-2까지 최대로 마시기 [..., X, O]
# 3. N과 N-1은 마시고 N-2는 안 마시고 N-3까지 최대로 마시기 [..., X, O, O]

for i in range(n):
    if i == 0:
        dp[i] = wine[i]
    elif i == 1:
        dp[i] = max(dp[i], wine[i - 1] + wine[i])
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

print(dp[n-1])

# 30840KB	80ms