# 브루트 포스
import sys

input = sys.stdin.readline

def solution():
    """
    idea > 
    1) i를 분해합 하였을때 n이 나오려면 i <= n 이어야함 
    2) 문자열을 list() 의 인자로 넣을 경우 한 문자씩 분리된 리스트를 받을 수 있음
    3) 숫자 -> 문자열 -> 리스트 로 각 자리수 합을 구하기
    """
    n = int(input())

    for i in range(1, n):
        if n == sum(list(map(int, list(str(i))))) + i:
            return i
        
    return 0

print(solution())