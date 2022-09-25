"""
- 우선순위 큐

idea> (절댓값, 원래 값) 형태로 저장
- heapq는 튜플 혹은 리스트 형태로 값이 들어오는 경우 차례대로 값을 비교
- 절댓값이 같으면 원래 값의 대소를 비교
"""
import heapq as hq
import sys

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if q:
            print(hq.heappop(q)[1])
        else:
            print(0)
        continue

    hq.heappush(q, (abs(num), num))
