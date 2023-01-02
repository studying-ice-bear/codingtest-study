import sys

# A에서 B로 버스를 타고 최소 비용으로 이동하는 방법을 알아내서, 이동 비용, 경유도시 수, 경유 도시 이름을 반환

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

INF = int(1e9)
route = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    dep, des, cost = map(int, sys.stdin.readline().rstrip().split())  # departure, destination
    if route[dep][des] > cost:
        route[dep][des] = cost

t_dep, t_des = map(int, sys.stdin.readline().rstrip().split())  # target

# print(n, m, route, t_des, t_dep)

visited = [False for _ in range(n + 1)]
d = [INF for _ in range(n + 1)]  # 최소 비용
path = [t_dep for _ in range(n + 1)]  # 경로
count = [0] * (n + 1)


def get_small_index():
    minimum = INF
    index = 0
    for i in range(1, n + 1):
        if d[i] < minimum and not visited[i]:
            minimum = d[i]
            index = i
    return index


# 이거 max + 람다로 표현할 수 있을까?

def dijkstra(start):
    for i in range(1, n + 1):
        d[i] = route[start][i]
        count[i] += 1

    visited[start] = True
    for _ in range(n - 1):
        cur = get_small_index()
        visited[cur] = True
        for j in range(1, n + 1):
            if not visited[j]:
                if d[cur] + route[cur][j] < d[j]:  # a -> b -> c VS a -> c
                    d[j] = d[cur] + route[cur][j]
                    path[j] = cur
                    count[j] = count[cur] + 1


dijkstra(t_dep)

# print(d, visited)

min_cost = d[t_des]  # 최소비용

# 경로 역추적
track = [t_des]
prev = t_des
for _ in range(count[t_des]):
    track.append(path[prev])
    prev = path[prev]

#  최소비용, 최소비용 경로에 속하는 도시의 개수, 최소비용 경로에 속하는 도시
print(str(min_cost), len(track), ' '.join(map(str, track[::-1])), sep='\n')

# 38584KB	492ms
