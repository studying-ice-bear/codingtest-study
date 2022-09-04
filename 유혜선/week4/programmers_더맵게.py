"""
- 힙
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/42626
규칙 >
스코빌 지수가 가장 낮은 음식 두개를 섞어서 새로운 음식을 만드는 과정을 반복하여
모든 음식의 스코빌 지수가 k 이상일때 섞은 횟수를 반환

아이디어 > 최소힙 이용

"""
import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0
    while True:
        lowest = hq.heappop(scoville)
        if lowest >= K:
            return cnt

        if len(scoville) == 0:
            return -1

        lowest2 = hq.heappop(scoville)

        hq.heappush(scoville, lowest + (lowest2 * 2))
        cnt += 1

print(solution([1, 2, 3, 9, 10, 12], 7))