import sys

T = int(sys.stdin.readline().rstrip())

# 1. 중복순열도 구해야했다.
# for _ in range(T):
#     n = int(sys.stdin.readline().rstrip())
#     answer = 0
#
#     for i in range(n // 1 + 1):
#         for j in range(n // 2 + 1):
#             for k in range(n // 3 + 1):
#                 if i * 1 + j * 2 + k * 3 == n:
#                     print(n, i, j, k)
#                     answer += 1
#     print(answer)


# 2. 점화식으로 풀 수 있다고 한다.
# 1 -> 1 (1)
# 2 -> 1+1, 2 (2)
# 3 -> 1+1+1, 1+2, 2+1, 3 (4)
# 4 -> 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 1+3, 3+1, 2+2 (7)
# 5 -> 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 1+1+3, 1+3+1, 3+1+1, 2+3, 3+2 (13)
# 총 개수를 가지고 f(n) = f(n-1) + f(n-2) + f(n-3) 라는 점화식이 나온다.

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n - 1) + dp(n - 2) + dp(n - 3)

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp(n))