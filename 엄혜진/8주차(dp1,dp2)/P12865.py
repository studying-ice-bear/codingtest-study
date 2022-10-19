import sys

N, K = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().rstrip().split())))
# print(N, K, items)

dp = [[0 for _ in range(K + 1)] for j in range(N)]
# print(len(dp), len(dp[0])) # N, K
# dp = [[0] * (K + 1)] * N # 얕은 복사가 일어나서 변경 사항이 모든 행에 적용된다... 왜 저랬지...
# print(dp)

for i in range(N):
    w, v = items[i]
    # print(w, v)
    for j in range(1, K + 1):
        if j >= w:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])
        elif j < w:
            dp[i][j] = dp[i - 1][j]
    # print(i, j, dp)

# for i in range(1, N + 1):
#     w, v = items[i]
#     for j in range(1, K + 1):
#         if w < j:
#             dp[i][j] = dp[i - 1][j]
#         elif w == j:
#             dp[i][j] = max(dp[i - 1][j - w], v)
#         print(i, j, dp[i][j])

# print(dp)
print(dp[N - 1][K])
