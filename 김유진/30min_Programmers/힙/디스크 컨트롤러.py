import heapq
def solution(jobs):
    answer = 0
    return answer

'''
혜선님 설명
[디스크 컨트롤러]
요청 큐 = deq
대기 큐 = heap

현재 시간 = 0


요청이 왔을 때
- 요청이 온 시간보다 현재 시간이 같거나 작을때
    - 대기 큐에 작업이 없다면 (비어있다면)
        - 요청을 수행 (요청 시간 + 수행 시간 = 현재 시간)
    - 대기 큐에 작업이 있다면
        - 대기 큐에서 수행 시간이 제일 적은 요청을 꺼내서 수행 (현재 시간 + 수행시간 = 현재 시간)
        - 제일 적은 요청을 수행 했는데도 현재 시간이 먼저 온 요청 시간보다 작거나 같다면
            - 요청을 요청 큐에 다시 집어 넣음
        - 제일 적은 요청을 수행했을 때 현재 시간이 먼저 온 요청 시간보다 큰 경우
            - 대기 큐에 현재 요청을 집어 넣음
- 요청이 온 시간보다 현재 시간이 클때
    - 대기 큐에 집어 넣음

위 과정을 요청 큐가 빌 때까지 계속 진행
이후 대기 큐를 돌며 시간 계산 및 평균 시간 계산
'''
