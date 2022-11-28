import sys

n = int(sys.stdin.readline().rstrip())
memo = [0] * 1001
memo[1] = 1
memo[2] = 2

for i in range(3, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n] % 10007)

# 재귀로 풀었다가 재귀호출횟수 초과가 나서 메모이제이션 방법으로 변경했다.
# 근데 문제도 제대로 안 읽고 나머지를 구하지 않고 제출해 버렸다. 문제 좀 제대로 읽고 풀어야한다..!
