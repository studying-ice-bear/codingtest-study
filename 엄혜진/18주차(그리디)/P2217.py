import sys

n = int(sys.stdin.readline().rstrip())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline().rstrip()))

# print(n, rope)

rope.sort(reverse=True)
# print(rope)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, rope[i - 1] * i)

print(answer)

# 문제를 이해하는 것이 제일 어려웠다.
# 로프를 중량 순으로 정렬해두고 두번째 로프를 가지고 든다고 생각하면,
# 두번째 로프와 첫번째 로프를 가지고 두번째 로프의 최대중량 / 2를 버틸 수 있을 것이다.
# 세번째 로프를 가지고 든다면, 1, 2, 3번 째 로프를 가지고 세번째 로프의 최대중량 / 3을 버틸 수 있을 것이다.
