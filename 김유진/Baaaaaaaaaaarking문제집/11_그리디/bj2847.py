import sys

N = int(sys.stdin.readline())

score = []
for _ in range(N):
    score.append(int(sys.stdin.readline()))

answer = 0
high = score[-1]
minus = [0] * N
for i in range(N-2, -1, -1):
    # print(high, score[i])
    if high < score[i]:
        answer += score[i] - high + 1
        score[i] = high - 1
    elif high == score[i]:
        score[i] -= 1
        answer += 1

    high = score[i]
# print(score)
print(answer)

'''
레벨을 난이도 순으로 배치
쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우가 있다.
특정 레벨의 점수를 감소


3
5: 4-1 -> 3
5: 5 == 5 -> 5-1 = 4
5 
'''

