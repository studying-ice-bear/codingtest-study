"""
- 그래프와 순회(BFS)

idea> 
- 게임판은 1차원배열로 확인
- 사다리나 뱀이 나오면 해당 지점과 도착지점도 같이 visited 처리 해줘야함
- 시작은 1부터
"""
import sys
from collections import deque as dq
input = sys.stdin.readline

def BFS():
    q = dq([1])
    while q:
        i = q.popleft()
        if i == 100:
            break

        for d in range(1, 7):
            di = i + d
            if di <= 100 and visited[di] == 0:
                visited[di] = visited[i] + 1
                if ladders[di] != 0:
                    # 사다리가 있으면
                    if visited[ladders[di]] != 0:
                        visited[ladders[di]] = min(visited[ladders[di]], visited[di])
                    else:
                        visited[ladders[di]] = visited[di]
                    q.append(ladders[di])
                elif snakes[di] != 0:
                    # 뱀이 있으면
                    if visited[snakes[di]] != 0:
                        visited[snakes[di]] = min(visited[snakes[di]], visited[di])
                    else:
                        visited[snakes[di]] = visited[di]
                    q.append(snakes[di])
                else:
                    # 둘 다 없으면
                    q.append(di)

ladders = [0] * 101
snakes = [0] * 101
visited = [0] * 101
n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

BFS()

print(visited[100])
