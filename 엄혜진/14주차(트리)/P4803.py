import sys
from collections import deque


def print_tree(case_num, count):
    print('Case ', case_num, ': ', sep='', end='')

    if count == 0:
        print('No trees.')
    elif count == 1:
        print('There is one tree.')
    elif count > 1:
        print('A forest of', count, 'trees.', sep=' ')


case = 1
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)  # 함수 안에서 방문기록을 관리하면 같은 트리를 여러번 카운트 하게 된다.
    tree_count = 0


    def is_tree(start):
        result = True

        dq = deque()
        dq.append(start)

        while dq:
            cur = dq.popleft()
            if visited[cur]:
                result = False
            visited[cur] = True
            for k in graph[cur]:
                if not visited[k]:
                    dq.append(k)

        return result


    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(i):
                tree_count += 1

    print_tree(case, tree_count)

    case += 1
