import heapq as hq
import sys

input = sys.stdin.readline

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    q = []
    time = 0
    duration = 0
    for job in jobs:
        hq.heappush(q, job[::-1])
        if time < job[0]:
            time = job[0]
            while q:
                d, a = hq.heappop(q)
                if time >= a:
                    time += d
                    duration += time - a
                else:
                    hq.heappush([d, a])
                    break
    while q:
        d, a = hq.heappop(q)
        if time < a:
            time = a + d
            duration += a + d
        else:
            time += d
            duration = time - a
    return int(duration / len(jobs))

print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
