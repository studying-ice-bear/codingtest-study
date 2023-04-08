from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(pickNum, num):
    global result
    val = 0

    if pickNum == M:
        for h in house:
            hr, hc = h[0], h[1]
            dist = 2 * N

            for c in select:
                cr, cc = c[0], c[1]
                tmp = abs(hr - cr) + abs(hc - cc)

                if tmp < dist:
                    dist = tmp

            val += dist

        if val < result:
            result = min(val, result)
            return

    for idx in range(num, K):
        select.append(chicken[idx])
        dfs(pickNum+1, idx+1)
        select.pop()


chicken = deque()
house = deque()

select = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

K = len(chicken)            # 치킨 집의 개수
result = N*2*len(house)     # 총 치킨 거리 값

for t in range(K):
    dfs(0, t)

print(result)
