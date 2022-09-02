"""
- 큐, 덱

⭐ 큐에 넣는 값을 정수형으로 변환하여 넣을 경우 메모리 down, 시간 up 
( 그냥 str 형으로 넣는 경우 메모리 up, 시간 down )
"""

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
    req = input().split()
    if req[0] == "push":
        q.append(int(req[1]))
    
    elif req[0] == "pop":
        print(q.popleft()) if q else print(-1)
    
    elif req[0] == "size":
        print(len(q))
    
    elif req[0] == "empty":
        print(1) if not q else print(0)
    
    elif req[0] == "front":
        print(q[0]) if q else print(-1)
    
    else:
        print(q[-1]) if q else print(-1)