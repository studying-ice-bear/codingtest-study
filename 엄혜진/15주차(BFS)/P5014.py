import sys

# 도저히 감이 안 와서 구글링해서 코드를 살짝 봤다. 1차원 배열에서 BFS로 푸는 거 같았다.
# 79172KB	848ms
# 처음에 생각했던것 보다 어려운 문제는 아니었다.
# 2차원에서 1차원으로 바뀐것 밖에 없는데 왜 그렇게 어려워했는지, 지금 생각하면 어이가 없다.

from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())
# print(f, s, g, u, d)


visited = [0 for _ in range(f + 1)]
count = [0 for _ in range(f + 1)]


def bfs(start):
    dq = deque()

    dq.append(start)
    visited[start] = 1

    while dq:
        current = dq.popleft()

        if current == g:
            return count[current]

        for move in [current + u, current - d]:
            if 0 < move <= f and not visited[move]:
                dq.append(move)
                visited[move] = 1
                count[move] = count[current] + 1

    if count[g] == 0:
        return "use the stairs"


print(bfs(s))
