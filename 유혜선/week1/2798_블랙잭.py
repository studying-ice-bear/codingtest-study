# 브루트 포스
from itertools import combinations as cb
import sys

input = sys.stdin.readline

def solution_1():
    """
    idea> 3중 for문으로 완전 탐색
    """
    n, m = map(int, input().split())
    card_list = list(map(int, input().split()))

    answer = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = card_list[i] + card_list[j] + card_list[k]
                if total <= m:
                    answer = max(total, answer)

    return answer


def solution_2():
    """
    idea > 순서 상관 없이 3개의 조합을 구해서 (combinations) 그 합이 m과 가까운지 확인
    """
    n, m = map(int, input().split(" "))
    cards = list(map(int, input().split(" ")))

    cases = list(cb(cards, 3))
    answer = 0
    for case in cases:
        sub = sum(case)
        if sub < m:
            answer = max(sub, answer)
        elif sub > m:
            continue
        else:
            answer = sub
            break

    return answer


print(solution_1())
print(solution_2())


# 시간과 공간 모두 3중 for문이 적게 나옴 !
