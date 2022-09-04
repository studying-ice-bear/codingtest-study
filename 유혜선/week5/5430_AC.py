"""
- 큐, 덱

idea> 'R'의 경우 deque.reverse()를 사용하면 시간초과
=> bool 값으로 reverse=True이면 'D'=> pop(), False이면 'D' => popleft()
"""

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    f = input()
    n = int(input())
    if n == 0:
        temp = input()
        arr = deque([])
    else:
        arr_str = input()
        arr = deque(arr_str[1:len(arr_str)-2].split(","))
    
    is_error = False
    is_reversed = False
    for action in f:
        if action == "R":
            is_reversed = not is_reversed
        
        if action == "D":
            if len(arr) == 0:
                is_error = True
                break
            
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()
    
    if is_error:
        print("error")
    
    else:
        print("[", end="")
        if is_reversed:
            print(','.join(list(arr)[::-1]), end="")
        else:
            print(','.join(arr), end="")
        print("]")