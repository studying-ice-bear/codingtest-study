"""
- 입국심사 (이분탐색)
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/43238
규칙 > n명을 모두 심사하는 최소 시간을 구하세요.

아이디어 > 시간을 기준으로 이분 탐색하자!
- 결국 사람들을 모두 심사하는데는 mid만큼의 시간이 걸리고,
- 각 심사관은 mid를 time으로 나눈 만큼 사람을 심사할 수 있다.
- 심사관별 심사할 수 있는 사람의 합이 n이 되면 그만큼 시간이 걸린다고 생각하면 된다.
"""
def solution(n, times):
    start = 0
    end = max(times) * n    # 가장 오래 걸리는 심사관한테 n명이 모두 심사를 받는 경우

    while start < end:
        mid = (start + end) // 2
        sub_total = 0   # 심사관이 심사하는 사람의 total
        for time in times:
            sub_total += (mid // time)
            if sub_total > n:
                break
        if sub_total >= n:
            end = mid
        else:
            start = mid + 1
    # print(start, end)    
    return (start + end) // 2



print(solution(6, [7, 10])) # 28