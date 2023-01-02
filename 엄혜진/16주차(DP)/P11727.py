import sys

n = int(sys.stdin.readline().rstrip())

memo = [0] * 1001
memo[1] = 1
memo[2] = 3
memo[3] = 5

for i in range(4, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2] * 2

print(memo[n] % 10007)

# 규칙을 도저히 모르겠어서 그냥 검색해버림...
# 이젠 알긴 했는데 다시 풀 때도 규칙을 찾을 수 있을런지 일말의 기대도 안 든다.
