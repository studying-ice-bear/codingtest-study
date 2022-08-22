"""
- Backtracking

- idea> DFS로 풀기
visited를 연산자 각각의 개수를 저장하는 dict를 이용해서 DFS 구현
* INF => 연산의 결과는 늘 -10e9 <= result <= 10e9 이므로 INF = 10e9 + 1로 지정
"""

import sys
input = sys.stdin.readline

INF = int(10e9 + 1)

n = int(input())
nums = list(map(int, input().split()))
ops = {i: int(val) for i, val in enumerate(input().split())}
max_val = -INF
min_val = INF
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a < 0:
        return -(abs(a) // b)
    else:
        return a // b

def DFS(depth, val, op):
    global n, max_val, min_val
    if 0 < depth < n:
        if op == 0:
            val = plus(val, nums[depth])
        elif op == 1:
            val = minus(val, nums[depth])
        elif op == 2:
            val = multiply(val, nums[depth])
        else:
            val = divide(val, nums[depth])
    
    if depth == n-1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    for i in range(4):
        if ops[i] != 0:
            ops[i] -= 1
            DFS(depth + 1, val, i)
            ops[i] += 1


DFS(0, nums[0], -1)
print(max_val)
print(min_val)