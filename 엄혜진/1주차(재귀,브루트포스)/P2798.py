n, m = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

answer = 0

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                answer = max(answer, total)

print(answer)

# 더위 먹었나 문제 푸는데 오래 걸렸다.
# 조합인건 알겠는데 코드로 도출하는 과정이 어려웠다.
# 그치만 알고보니 이만큼 시간 걸린게 바보다... 이런건 5분 내로 풀자.

# [ 다른 풀이 ]
# 파이썬 itertools 라이브러리에 제공되는 조합 메소드: iterstools.combinations(iterable, r)
# Doc: https://docs.python.org/3/library/itertools.html?highlight=itertools%20combinations#itertools.combinations
# 입력 iterable로 조합을 구한다. 원소들이 정렬되어 있다면 결과값도 정렬되어 나온다.
# 각 원소는 위치로 구별된다.
import itertools

for combination in itertools.combinations(cards, 3):
    total = sum(combination)
    if total <= m:
        answer = max(answer, total)

print(answer)
