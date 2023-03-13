import sys

n = int(input())
solution = list(map(int, input().split()))

start = 0
end = n-1
answer = sys.maxsize
start_answer = 0
end_answer = 0

while True:
    if start >= end:
        break
    
    temp = solution[start] + solution[end]
    if abs(temp) < answer:
        answer = abs(temp)
        start_answer = start
        end_answer = end
        if temp == 0: break
    
    if temp > 0: end -= 1
    elif temp < 0: start += 1

print(solution[start_answer], solution[end_answer])


'''
투포인터 - start, end로 세팅
두 값의 합이 음수이면 0에 더 가까워지기 위해서 start 포인터가 이동해야하고
두 값의 합이 양수이면 0에 더 가까워지기 위해서 end 포인터가 이동해야한다.
'''