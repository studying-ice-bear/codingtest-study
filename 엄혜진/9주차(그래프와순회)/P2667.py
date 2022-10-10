import sys

sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(N):
    graph.extend(list(map(str, sys.stdin.readline().rstrip().split())))
visited = [[0 for j in range(N)] for i in range(N)]

# print(N, graph, visited)


def check_dfs(E, i, j, current):
    if i < 0 or i >= N or j < 0 or j >= N:
        # print(i, j)
        return 0

    visited[i][j] = current
    # print(i, j, visited)
    result = 1
    if 0 <= i - 1 < N and graph[i - 1][j] == '1' and visited[i - 1][j] == 0:
        result += check_dfs(E, i - 1, j, current)
    if 0 <= j - 1 < N and graph[i][j - 1] == '1' and visited[i][j - 1] == 0:
        result += check_dfs(E, i, j - 1, current)
    if 0 <= i + 1 < N and graph[i + 1][j] == '1' and visited[i + 1][j] == 0:
        result += check_dfs(E, i + 1, j, current)
    if 0 <= j + 1 < N and graph[i][j + 1] == '1' and visited[i][j + 1] == 0:
        result += check_dfs(E, i, j + 1, current)

    return result


count = 0
answer = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == 0:
            count += 1
            # print(count)
            answer.append(check_dfs(graph, i, j, count))

            # for k in range(len(visited)):
            #     print(visited[k])
            # print()

# for i in range(len(visited)):
#     print(visited[i])

print(count)
print('\n'.join(map(str, sorted(answer))))

# 31084KB	72ms