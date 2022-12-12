import sys

n = int(sys.stdin.readline().rstrip())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline().rstrip()))
# print(n, score)

answer = 0
for i in range(n - 1, -1, -1):
    if i - 1 >= 0 and score[i] <= score[i - 1]:
        target = score[i] - 1
        answer += score[i - 1] - target
        score[i - 1] = target

print(answer)

# 뒤에서 부터 시작해야한다는 건 눈치챘지만,
# 전체적인 로직은 https://www.acmicpc.net/board/view/13218 이 글 답변에서 알았다.
# 다음에는 로직까지 스스로 알아내길 바란다...
