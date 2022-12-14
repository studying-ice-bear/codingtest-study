import sys
# import itertools

N = int(sys.stdin.readline().rstrip())

# tiles = ['00', '1']
# print(list(itertools.product([0, 1], repeat=N)))
# 중복순열인가 싶어서 product를 사용했지만, 수열의 개수를 따져야 했기 때문에 아닌 듯했다..
# 그래서 검색했더니 이게 웬걸 점화식을 구해야한다고 한다.. 제일 약한게 점화식인데..

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[N])

# 타일이 될 수 있는 모든 경우를 따져보면
# 수열의 개수가 1일 때: 1 (1개)
# 수열의 개수가 2일 때: 00, 11 (2개)
# 수열의 개수가 3일 때: 001, 100, 111 (3개)
# 수열의 개수가 4일 때: 0000, 0011, 1100, 1001, 1111 (5개)
# 수열의 개수가 5일 때: 00001, 00100, 10000, 00111, 10011, 11001, 11100, 11111 (8개)
# ...
# 1, 2, 3, 5, 8, ... 보면 피보나치 수열이다.
# 답의 규칙을 찾는 것이 푸는 방법이었다.

