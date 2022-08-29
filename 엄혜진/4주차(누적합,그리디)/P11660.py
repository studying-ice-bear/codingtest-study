import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

table = [[0] * (N + 1)]
for l in range(N):
    line = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    table.append([line[i] + table[l][i] for i in range(N + 1)])  # 세로로 누적합 만들기

# print(table)

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    # print(x1, y1, x2, y2)
    answer = 0
    for i in range(y1, y2 + 1):
        answer += table[x2][i] - table[x1 - 1][i]
        # print(answer, i, table[x2][i], table[x1 - 1][i])
    sys.stdout.write(str(answer) + '\n')

# pypy3으로 하니 맞았다..
# 메모리 125328KB	시간 1012ms

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# memo = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         memo[i][j] = memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1] + arr[i - 1][j - 1]
#
# answer = []
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     ans = memo[x2][y2] - memo[x1 - 1][y2] - memo[x2][y1 - 1] + memo[x1 - 1][y1 - 1]
#     answer.append(ans)
# print('\n'.join(map(str, answer)))

# 나는 | 모양으로 누적합을 메모했는데, 시간이 월등히 빠른 코드는 ⏌ 모양으로 누적합을 구했다.
# 담에는 꼭 이렇게 풀자!