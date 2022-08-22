import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
answer = []
temp = []

def dfs():
    if len(temp) == m:
        for num in temp:
            print(num, end=' ')
        print('')
        return
    
    for i in range(1, n+1):
        if len(temp) == 0 or i >= temp[len(temp)-1]:
            temp.append(i)
            dfs()
            temp.pop()

dfs()