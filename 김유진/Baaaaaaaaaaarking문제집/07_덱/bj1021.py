from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
arr = deque([i for i in range(1, N+1)])

answer = 0

for n in num:
    while True:
        if arr[0] == n:
            arr.popleft()
            break
        else:
            if arr.index(n) > len(arr) // 2:
                while arr[0] != n:
                    a = arr.pop()
                    arr.appendleft(a)
                    answer += 1
            else:
                while arr[0] != n:
                    a = arr.popleft()
                    arr.append(a)
                    answer += 1

print(answer)

'''
10 3
1 2 3

10 3
2 9 5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[2, 3, 4, 5, 6, 7, 8, 9, 10, 1] -> 2
[3, 4, 5, 6, 7, 8, 9, 10, 1]

[1, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 1, 3, 4, 5, 6, 7, 8, 9]
[9, 10, 1, 3, 4, 5, 6, 7, 8] -> 9
[8, 9, 10, 1, 3, 4, 5, 6, 7]

[7, 8, 9, 10, 1, 3, 4, 5, 6]
[6, 7, 8, 9, 10, 1, 3, 4, 5]
[5, 6, 7, 8, 9, 10, 1, 3, 4] -> 5

'''