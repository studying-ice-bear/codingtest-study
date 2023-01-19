import sys
N, M = map(int, sys.stdin.readline().split())

pokemon = {}
numbers = {}

for i in range(N):
    ss = sys.stdin.readline().strip()
    pokemon[i] = ss
    numbers[ss] = i+1

for j in range(M):
    problem = sys.stdin.readline().strip()
    if problem.isnumeric():
        print(pokemon[int(problem)-1])
    else:
        print(numbers.get(problem))

'''
문제링크: https://www.acmicpc.net/problem/1620
- 다른 풀이: zip 사용하기
def sol():
    input = sys.stdin.readline
    n, m =map(int, input().split())
    dd = [0]+[input().strip() for i in range(n)]
    print(dd)
    
    d = dict(zip(dd, range(n+1)))
    ans = [dd[int(t)] if (t := input().strip()).isdigit() else str(d[t]) for i in range(m)]
    print("\n".join(ans))

sol()
'''