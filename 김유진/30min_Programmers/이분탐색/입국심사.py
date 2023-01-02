# 아이디어가 뭐였지?
# 시간에서 이분탐색하기

def solution(n, times):
    low = 0
    high = max(times) * n
    while low <= high:
        middle = (low + high) // 2
        canDo = 0
        for time in times:
            canDo += middle // time # 시간을 time으로 나누어서
            if canDo >= n:   # 시간이 찾으려는 명수보다 크면 break
                break

        if canDo >= n:
            high = middle
        else:
            low = middle + 1

    answer = low
    return answer




if __name__=="__main__":
    solution(6, [7, 10])