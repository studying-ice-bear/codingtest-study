# 아이디어가 뭐였지?
#
def solution(n, times):
    low = 0
    high = max(times) * n
    while low <= high:
        middle = (low + high) // 2
        canDo = 0
        for time in times:
            canDo += middle // time

        if canDo >= n:
            high = middle
        else:
            low = middle + 1

    answer = low
    return answer




if __name__=="__main__":
    solution(6, [7, 10])