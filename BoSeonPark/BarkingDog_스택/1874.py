import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

nums = deque([int(input()) for _ in range(n)])
stack = []
answer = []
start = 1

while nums:
    end = nums.popleft()
    
    if len(stack) == 0:
        for i in range(start, end + 1):
            stack.append(i)
            answer.append('+')
        stack.pop()
        answer.append('-')
        start = end + 1
    elif stack[-1] == end:
        stack.pop()
        answer.append('-')
    elif stack[-1] < end:
        for i in range(start, end + 1):
            stack.append(i)
            answer.append('+')
        stack.pop()
        answer.append('-')
        start = end + 1
    elif stack[-1] > end:
        break

if len(answer) != n * 2:
    print('NO')
else:
    for f in answer:
        print(f)
    
    
    

