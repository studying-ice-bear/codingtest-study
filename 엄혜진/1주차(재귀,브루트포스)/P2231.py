n = int(input())

answer = 0

for num in range(n, 1, -1):
    num_sum = sum(map(int, str(num)))
    if n == num_sum + num:
        answer = num
        # 216의 경우 정답인 198 이외에도 207(2+0+7+207=216)이 존재하기 때문에 가장 작은 수를 찾을 수 있도록 모든 경우를 확인해야한다.

print(answer)


# range(start, stop[, step])
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=range#range

# string to int: str() 함수 사용
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=str#str