import sys

# sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


# print(tree)

def dfs(cur, t, p):
    # 1. 재귀 버전 -> 156168KB	416ms
#     for k in t[cur]:
#         if p[k] == 0:
#             parent[k] = cur
#             dfs(k, t, p)

    # 2. 스택 버전 -> 47764KB	344ms
    stack = [[cur, t, p]]
    while stack:
        C, T, P = stack.pop()
        for k in T[C]:
            if P[k] == 0:
                P[k] = C
                stack.append([k, T, P])

parent[1] = 1  # 루트노드는 1 (결과값에 지장없음)
dfs(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])

# 파이썬은 passed by assignment다.
# 가변 객체(list, dict, etc)는 call by reference
# 불변 객체(int, str, etc)는 call by value
