"""
- 스택 & 큐
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/12906
규칙 >
같은 숫자가 "연속"해서 나오는 경우 하나만 남기고 제거 (숫자 중복 제거 x)
순서를 보장하며 배열로 반환

아이디어 >
1 주어진 arr를 deque로 변환하여 
stack에 차근 차근 넣기 (단 stack의 마지막 원소와 비교하여 같은 경우(연속)는 넣지 않음)
2 인덱스를 하나 하나 증가시켜 스택에 넣기
"""
from collections import deque as dq

def solution(arr):
    answer = []
    arr = dq(arr)
    
    while arr:
        val = arr.popleft()
        if not answer or answer[-1] != val:
            answer.append(val)
            
    return answer


print(solution([1,1,3,3,0,1,1]))    # [1, 3, 0, 1]
print(solution([4,4,4,3,3]))    # [4, 3]