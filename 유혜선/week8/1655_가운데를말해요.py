"""
- 우선순위 큐

idea> 가운데 값을 알기 위해 left queue, right queue 구현
- left queue 는 max_heap으로 left queue의 0번 인덱스가 중간값이고 중간값 보다 작은 값을 넣는 큐
- rigth queue 는 min_heap으로 left queue의 0번 인덱스(중간값)보다 큰 값들을 넣는 큐
- 수를 위 조건에 맞게 넣은 후 반복문으로 큐 개수 조정

[반복문 종료조건]
- left queue의 길이는 항상 넣은 수의 개수의 절반(홀수의 경우 올림)
- right queue의 길이는 넣은 수의 개수의 절반(홀수의 경우 내림)
ex.
총 넣은 수를 5라고 할때
len(left_queue) == 3
len(right_queue) == 2 

"""
import heapq as hq
import sys
import math
input = sys.stdin.readline

def solution(N):
    lq = []
    rq = []
    for i in range(N):
        num = int(input())
        if lq and lq[0][1] < num:
            hq.heappush(rq, (num, num))
        else:
            hq.heappush(lq, (-num, num))

        while True:
            if len(lq) == math.ceil((i + 1) / 2) and len(rq) == (i + 1) // 2:
                break
            
            if len(rq) > (i + 1) // 2:
                val, _ = hq.heappop(rq)
                hq.heappush(lq, (-val, val))
            else:
                _, val = hq.heappop(lq)
                hq.heappush(rq, (val, val))
        print(lq[0][1])

    return

if __name__ == '__main__':
    N = int(input())
    solution(N)