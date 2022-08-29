import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

temperature = list(map(int, sys.stdin.readline().rstrip().split()))

# pre_sum = []
# for i in range(N - K + 1):
#     pre_sum.append(sum(temperature[i:i + K]))
# # print(pre_sum)
#
# sys.stdout.write(str(max(pre_sum)))
# 시간초과가 난다. sum 때문인듯. 누적합으로 접근한다.

pre_sum = [0]
temp = 0
for i in range(N):
    temp += temperature[i]
    pre_sum.append(temp)

# print(pre_sum)

k_sum = []
for i in range(N - K + 1):
    k_sum.append(pre_sum[i + K] - pre_sum[i])

# print(k_sum)

sys.stdout.write(str(max(k_sum)))

# sum 때문인게 맞았음.