import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))


# print(N, A)

# 1. 틀림
# answer = 0
# dp = [0] * N
# for i in range(N):
#     max_length = 1
#     max_cur = A[i]
#     for j in range(i + 1, N):
#         if max_cur < A[j]:
#             max_length += 1
#             max_cur = A[j]
#     dp[i] = max_length
#
# print(max(dp))

# 2. 시간 초과
# def calc(idx, length, maximum):
#
#     if idx == N:
#         print(idx, length, maximum)
#         return length
#
#     if A[idx] > maximum:
#         return max(calc(idx + 1, length + 1, A[idx]), calc(idx + 1, length, maximum))
#     else:
#         return calc(idx + 1, length, maximum)
#
#
# print(calc(0, 0, 0))

# 3. 블로그 참고 30840KB	196ms
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(max(dp))

# 너무 간단해서 너무 허무하고 너무 놀랍다...