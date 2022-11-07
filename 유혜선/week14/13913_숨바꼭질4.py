import sys
from collections import deque as dq

input = sys.stdin.readline

a, b = map(int, input().split())
loc = [0] * (100001)
move = [-1] * len(loc)

def tracking(node):
    tracker = node
    answer = []
    while True:
        answer.append(tracker)
        if tracker == move[tracker]:
            break
        tracker = move[tracker]

    print(*answer[::-1])
    return

def bfs(node, target):
    q = dq([node])
    move[node] = node
    while q:
        cur = q.popleft()
        
        if cur == target:
            print(loc[cur])
            tracking(target)
            return

        for nxt in (2*cur, cur + 1, cur - 1):
            if 0 <= nxt < len(loc) and loc[nxt] == 0 and nxt != node:
                loc[nxt] = loc[cur] + 1
                move[nxt] = cur
                q.append(nxt)

    return

bfs(a, b)
