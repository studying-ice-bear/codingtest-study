import sys
N = int(sys.stdin.readline())

S = []

for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))

visited = [False for _ in range(N)]
answer = int(1e9)

def dfs(cnt, pos):
    global answer

    if cnt == N/2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):

                if visited[i] and visited[j]:
                    start += S[i][j]

                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        answer = min(abs(start-link), answer)
        return

    for i in range(pos, N):
        visited[i] = True
        dfs(cnt+1, i+1)
        visited[i] = False

dfs(0, 1)
print(answer)

