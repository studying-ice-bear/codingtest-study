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
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

