"""
Dynamic Programming

반례 모음(감사합니다 - !): https://raejoonee.tistory.com/15

※ 연속으로 3잔은 마실 수 없음

- idea > dp로 풀기
memo[i] 에는 [i번째 잔을 마시는 경우 최댓값, 마시지 않을 경우 최댓값] 을 저장한다.
1) i번째 잔을 마시는 경우 
1-1) (i - 2)번째 잔을 마시지 않고 (i - 1) 번째, i 번째 잔을 마신다.
1-2) (i - 2)번째 잔을 마시고 (i - 1)번째 잔을 마시지 않고, i 번째 잔을 마신다.

2) i번째 잔을 마시지 않는 경우
2-1) (i - 3)번째 잔은 마시지 않고, (i - 2)번째 잔과 (i - 1)번째 잔을 마신다.
2-2) (i - 1)번째 잔을 마신다.
2-3) (i - 1)번째 잔을 마시지 않는다.

3) i번째 잔이 비어 있는 경우
해당 잔은 마실 수 없으므로 
i-1번째 잔을 마시거나 / 마시지 않은 두 가지 경우 중 최댓값을 memo[i]의 배열로 저장한다.


틀린 부분을 알아냈던 반례>
1) 10 0 0 10 0 5 10 0 0 1 10 (답 36, 빈 잔이 있는 경우)
2) 6 1000 1000 1 1 1000 1000 (답 4000, 두 잔 연속 안 마시는 경우)
"""

import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

# memo = [[0, 0] for _ in range(n)]
# if n >= 1:
#     memo[0] = [wine[0], 0]
# if n >= 2:
#     memo[1] = [wine[1] + wine[0], wine[0]]
# if n >= 3:
#     memo[2] = [max(wine[2] + wine[1], wine[2] + wine[0]), wine[1] + wine[0]]
#     for i in range(3, n):
#         if wine[i] == 0:
#             val = max(memo[i-1])
#             memo[i] = [val, val]
#         else:
#             memo[i][0] = max(wine[i] + wine[i-1] + memo[i-2][1], memo[i-2][0] + wine[i])
#             memo[i][1] = max(memo[i-1][1], memo[i-1][0], wine[i-1] + wine[i-2] + memo[i-3][1])
# print(memo)
# print(max(memo[n-1]))

"""
- 보선님 풀이
1) 직전 포도주를 마시고, 지금 마시는 경우
2) 2번째 전 포도주를 마시고, 지금 마시는 경우
3) 지금 마시지 않는 경우(직전 경우 중 최댓값)

위 세 가지 경우를 memo에 저장해나가면서 최댓값 구하기
"""
memo = [[0, 0, 0] for _ in range(n)]

memo[0] = [wine[0]] * 3
memo[1] = [wine[0] + wine[1], wine[1], wine[0]]

for i in range(2, n):
    memo[i][0] = memo[i-1][1] + wine[i]
    memo[i][1] = memo[i-1][2] + wine[i]
    memo[i][2] = max(memo[i-1])

print(memo)
print(max(memo[n-1]))