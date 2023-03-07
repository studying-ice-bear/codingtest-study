# 순열 : 백트래킹으로 O(N)으로 풀기

# from itertools import permutations

n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)
 
def dfs():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            dfs()
            arr.pop()
            visited[i] = False

dfs()

# for permu in permutations(range(1,n+1), m):
#     print(*permu)

'''
# in 연산은 O(N) 걸리기 때문에 로직 살짝 바꾸자!

n, m = map(int, input().split())
arr = []
 
def dfs():
    if len(arr) == m:
        print(*arr) 
        return
    
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
'''