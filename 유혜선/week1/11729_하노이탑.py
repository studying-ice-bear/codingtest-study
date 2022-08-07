# 재귀
"""
idea > 
1, 2, 3번째 기둥이 있고 1번 기둥에서 3번으로 n개의 원판을 옮겨야 한다면
n-1개의 원판을 1번 기둥에서 2번 기둥으로 옮긴뒤 
제일 밑에 있는 원판(n번째 원판)을 1번 기둥에서 3번 기둥으로 옮긴 후
다시 n-1개의 원판을 2번 기둥에서 3번 기둥으로 옮겨야 한다.

여기서 중간 기둥(2번)을 mid = 6 - (첫번째 기둥(1) + 목표 기둥(3)) 으로 구한다.
"""
def hanoi(n, prev, next):
    mid = 6 - (prev + next)
    if n == 1:
        print(f"{prev} {next}")
    
    else:
        hanoi(n-1, prev, mid)
        hanoi(1, prev, next)
        hanoi(n-1, mid, next)

x = int(input())
hanoi(x, 2, 3)
