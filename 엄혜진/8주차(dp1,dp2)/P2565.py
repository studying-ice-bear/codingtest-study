import sys

N = int(input())

# 1.
# dp[i] 가 교차되지 않는다는 것은
# dp[1] ~ dp[i - 1]의 값이 dp[i]보다 작고, dp[i + 1] ~ dp[500] 값이 dp[i]보다 크다는 것이다
# 그래서 부분수열을 구하는 방식을 차용하면 될 거 같다.
# 그렇다면 여기서 제거할 선을 최소로 만들려면 어떻게 해야할까?
# 부분수열이 가장 긴 것을 찾아서 해당되지 않는 선들의 개수를 구하면 되지 않을까?
# 아니다.. 어디랑 교차했는지 확인해야하니까 복잡해진다

# wire = [0] * 501
# a_max, b_max = 0, 0
# for _ in range(N):
#     a, b = map(int, input().split())
#
#     a_max = max(a_max, a)
#     b_max = max(b_max, b)
#
#     wire[a] = b
# print(wire)
#
# dp = [0] * a_max

# 2. 블로그 참조 -> 30840KB	68ms
# 부분수열을 구하는게 맞다. 단, B 전봇대에서 구하는 것이다.

wire = []
for _ in range(N):
    wire.append(list(map(int, sys.stdin.readline().rstrip().split())))

wire.sort(key=lambda x: x[0])
# print(wire)

dp = [1] * N

for i in range(N):
    for j in range(i):
        if wire[i][1] > wire[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
