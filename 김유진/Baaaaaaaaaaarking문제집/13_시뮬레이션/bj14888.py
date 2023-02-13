'''
문제 링크: https://www.acmicpc.net/problem/14888
주어진 수의 순서를 바꾸면 안된다.
덧셈, 뺄셈, 곱셈, 나눗셈

2
5 6
0 0 1 0
output:
30
30

3
3 4 5
1 0 1 0
output:
35
17

6
1 2 3 4 5 6
2 1 1 1
output:
54
-24

'''

import sys
from itertools import permutations

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
op_num = list(map(int, sys.stdin.readline().split()))
op_list = ['+', '-', '*', '/']
op = []

maximum = -1e9
minimum = 1e9

for k in range(4):
    for i in range(op_num[k]):
        op.append(op_list[k])

def solve():
    global maximum, minimum
    for case in permutations(op, N-1):
        total = numbers[0]
        for r in range(1, N):
            if case[r-1] == '+':
                total += numbers[r]
            elif case[r-1] == '-':
                total -= numbers[r]
            elif case[r-1] == '*':
                total *= numbers[r]
            elif case[r-1] == '/':
                total = int(total / numbers[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth+1, total+numbers[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-numbers[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*numbers[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/numbers[depth]), plus, minus, multiply, divide-1)

# dfs(1, numbers[0], op[0], op[1], op[2], op[3])
solve()
print(maximum)
print(minimum)
