import sys

N = int(input())

words = []

for i in range(N):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words)) # 중복 제거

words.sort()
words.sort(key=lambda x: len(x))

# 람다식 사용법 헷갈려서 검색했는데 딱 이 문제를 예시로 들어줘서 답 스포 당함..
# sort(*, key=None, reverse=False)
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=sort#list.sort
# 람다 표현식
# Doc: https://docs.python.org/3/reference/expressions.html?highlight=lambda%20x#lambdas-1
# 먼저 사전식으로 정렬한 뒤 길이 순으로 정리하면, 사전식이 유지된 상태로 길이 순으로 정렬한다.

for word in words:
    sys.stdout.write(word + '\n')