n, m = map(int, input().split())
arr = []

def dfs():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1,n+1):
        if i not in arr and (not arr or i > arr[-1]):
            arr.append(i)
            dfs()
            arr.pop()

dfs()

'''
# 반복되는 코드
def dfs():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1,n+1):
        if arr:
            if i not in arr and i > arr[-1]:
                arr.append(i)
                dfs()
                arr.pop()
        else:
            arr.append(i)
            dfs()
            arr.pop()

'''