import sys

N = int(sys.stdin.readline().rstrip())
dp = [[0, [1]] for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]

    if i % 2 == 0 and dp[i][0] > dp[i // 2][0] + 1:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

    if i % 3 == 0 and dp[i][0] > dp[i // 3][0] + 1:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]

print(dp[N][0])

dp[N][1].reverse()
for i in dp[N][1]:
    print(i, end=' ')

# DP bottom-up 방식으로 해결했다.
# 1부터 N까지 확인하는 방법이므로, 1을 뺀다면 1을 더하는 것과 같다.
# 기본적으로 1을 더한다고 생각하고, 3을 나누거나 2를 나누는게 더 빨리 도달하는 방법이라면 그걸로 해결한다.
# 완전히 이해한 느낌은 아니다. 다음에는 아무것도 보지 않고 온전히 내힘으로 풀면 좋겠다.
