"""
- 분할정복

idea> 재귀 이용

<params>
r : 탐색 시작 위치(행)
c : 탐색 시작 위치(열)
k : 탐색 범위

- 범위의 맨 처음 원소를 기준 (flag)
- for문을 돌다가 flag와 값이 다르면 범위를 절반으로 줄여서 재탐색(k = k // 2)
- k // 2 만큼 step을 뛰면서 재귀 호출 
- 재귀 호출을 하게 될때(flag가 다를때) "(" 를 출력
- 재귀 호출을 다 끝내고(절반의 step만큼 재귀 호출한 후) ")" 출력한 후 return

ex)
arr =
1 1 1 1
1 1 1 0
0 0 0 0
0 0 0 0

1) r=0, c=0, k=4
arr[1][2]에서 flag(1)와 다름

=> "(" 출력
=> 2, 3, 4, 5번 과정 재귀 호출

2) r=0, c=0, k=2
=> 1 출력

3) r=0, c=2, k=2
arr[1][3]에서 flag(1)와 다름

=> "(" 출력
=> 3-1, 3-2, 3-3, 3-4 과정 재귀 호출

3-1) r=0, c=2, k=1
=> 1 출력
3-2) r=0, c=3, k=1
=> 1 출력
3-3) r=1, c=2, k=1
=> 1 출력
3-4) r=1, c=3, k=1
=> 0 출력

=> ")" 출력 후 return

4) r=2, c=0, k=2
=> 0 출력

5) r=2, c=2, k=2
=> 0 출력

=> ")" 출력 후 return

result = (1(1110)00)
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def dnc(r, c, k):
    
    flag = arr[r][c]
    for i in range(r, r + k):
        for j in range(c, c + k):
            if arr[i][j] != flag:
                print("(", end="")
                for dr in range(r, r + k, k//2):
                    for dc in range(c, c + k, k//2):
                        dnc(dr, dc, k//2)
                print(")", end="")
                return
    
    print(flag, end="")


dnc(0, 0, n)
