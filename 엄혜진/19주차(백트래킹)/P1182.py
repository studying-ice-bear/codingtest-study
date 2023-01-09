import sys
import itertools
from collections import deque

n, s = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

# print(n, s, num)

# 1. 브루트 포스 56700KB	488ms
# answer = 0
#
# for i in range(1, n + 1):
#     for c in list(itertools.combinations(num, i)):
#         if sum(c) == s:
#             answer += 1
#
# print(answer)

# 2.

# 2-1. 재귀버전 34088KB	284ms
answer = 0


def sum_sub1(cur, total):
    global answer

    if cur >= n:
        return

    if total + num[cur] == s:
        answer += 1

    sum_sub1(cur + 1, total + num[cur])
    sum_sub1(cur + 1, total)


sum_sub1(0, 0)
print(answer)


# 2-2. bfs버전 138424KB	676ms
def sum_sub2():
    result = 0
    dq = deque()
    dq.append((0, 0))
    while dq:
        cur, total = dq.popleft()
        if cur >= n:
            break

        if total + num[cur] == s:
            result += 1

        dq.append((cur + 1, total + num[cur]))
        dq.append((cur + 1, total))

    return result


print(sum_sub2())
