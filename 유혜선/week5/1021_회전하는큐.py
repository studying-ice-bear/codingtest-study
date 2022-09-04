"""
- 큐, 덱

idea> deque의 rotate 이용
q = deque([1, 2, 3, 4])
q.rotate(1) => [4, 1, 2, 3]  => 오른쪽으로 한칸씩 이동
q.rotate(-1) => [2, 3, 4, 1]  => 왼쪽으로 한칸씩 이동

뽑아내야하는 수의 위치가 len(q) // 2 초과일 경우 오른쪽으로 회전
이하일 경우 왼쪽으로 회전
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque([i for i in range(1, n+1)])

arr = list(map(int, input().split()))

answer = 0
cur = 0
for val in arr:
    idx = q.index(val)
    if idx <= (len(q) // 2):
        answer += idx
        q.rotate(-idx)
    else:
        move = len(q) - idx
        answer += move
        q.rotate(move)
    
    # print(q)
    q.popleft()
    


print(answer)