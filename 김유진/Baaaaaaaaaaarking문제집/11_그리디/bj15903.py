import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cards)

for _ in range(M):
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    heapq.heappush(cards, tmp)

print(sum(cards))


'''
N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
MIN = 10**7
card.sort()
count = 0

for i in range(N):
    for j in range(N):
        if count == M:
            break
        if card[i] == card[j]:
            continue
        total = card[i] + card[j]
        card[i] = card[j] = total
        print(card)
        total = sum(card)
        print(total)
        count += 1
print(total)
'''
'''
이 점수를 가장 작게 만드는 것이 놀이의 목표이다.

'''
