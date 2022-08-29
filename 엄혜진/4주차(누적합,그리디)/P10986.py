import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
# print(N, M, nums)

# answer = 0
# dp = [0]
# temp = 0
# for i in range(N):
#     temp += nums[i]
#     dp.append(temp)
#     for j in range(i + 1):
#         # print(i, ' - ', j)
#         if (dp[i + 1] - dp[j]) % M == 0:
#             answer += 1
#             # print('dp',dp,  dp[i + 1], dp[j], dp[i + 1] - dp[j], answer)
#     # print(dp)
#
# print(answer)
# 시간초과가 난다..
# 1시간째 모르겠어서 검색해봤는데 이게 뭔소리지..?

nums.append(0)
r = [0] * M  # remainers
for i in range(N):
    nums[i] += nums[i - 1]
    r[nums[i] % M] += 1

cnt = r[0]
print(r)
for i in r:
    cnt += i * (i - 1) // 2  # 이해를 못함...

print(cnt)
