# 브루트 포스
from sys import stdin

input = stdin.readline

def solution():
    """
    idea> 8x8 범위를 다 체크해서 색칠해야 할 칸의 개수를 세고 그 중에 최소값을 구하기
    W, B가 반복되는걸 토글로 구현 (단, 한 줄에 8개(짝수)이므로 줄바꿈이 있을때 한번 더 토글)
    ※ 체스판은 W로 시작하거나 B로 시작할 수 있으므로 이 경우도 확인해주어야함.
    """
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    toggle = {"W": "B", "B": "W"}
    answers = []
    for i in range(n-7):
        for j in range(m-7):
            for k in "WB":
                answer = 0
                first = k
                check = first
                for di in range(i, i+8):
                    for dj in range(j, j+8):
                        if board[di][dj] != check:
                            answer += 1
                        check = toggle[check]
                    check = toggle[check]
                answers.append(answer)
    
    print(answers)
    return min(answers)


print(solution())