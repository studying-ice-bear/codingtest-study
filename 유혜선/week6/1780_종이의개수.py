"""
- 분할정복

idea> 재귀 이용

<params>
r : 탐색 시작 위치(행)
c : 탐색 시작 위치(열)
k : 탐색 범위

- 범위의 맨 처음 원소를 기준 (flag)
- for문을 돌다가 flag와 값이 다르면 범위를 3분의 1로 줄여서 재탐색(k = k // 3)
- k // 3 만큼 step을 뛰면서 재귀 호출 

⭐ 쿼드트리 문제 변형

"""
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = {-1: 0, 0: 0, 1: 0}

def dnc(r, c, k):
    flag = paper[r][c]
    if k == 1:
        cnt[flag] += 1
        return

    for i in range(r, r+k):
        for j in range(c, c+k):
            if flag != paper[i][j]:
                for dr in range(r, r+k, k // 3):
                    for dc in range(c, c+k, k // 3):
                        dnc(dr, dc, k // 3)
                
                return
    
    cnt[flag] += 1

dnc(0, 0, n)
print(*cnt.values(), sep="\n")
