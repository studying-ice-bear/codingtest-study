import sys

s1 = input()
s2 = input()

dp = [0] * len(s1)

for i in range(len(s2)):
    cur = 0
    for j in range(len(s1)):
        if cur < dp[j]:
            cur = dp[j]
        elif s1[j] == s2[i]:
            dp[j] = cur + 1
    # print(s2[i], dp)

print(max(dp))