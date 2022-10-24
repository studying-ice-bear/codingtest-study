"""
- 그래프
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/49190
규칙 > 주어진 arrows에 따라 이동했을 때 생기는 공간(방)의 개수를 구해라.

아이디어 > 
- 방문한 지점에 다시 도달하게 되면 공간이 생길 가능성이 있다.
- 단, 지점을 같은 경로로 다시 지나게되면 공간이 생기는게 아니라 경로가 겹치게 된다.
- 따라서 지점의 방문 여부를 체크할때 현재 노드에서 다음 노드로 가는 경로를 기록해준다.
=> 현재노드의 배열에 다음 노드 추가, 다음 노드의 배열에 현재 노드 추가
- 대각선으로 지날때 노드가 아니라 이동하면서 생기는 경로가 겹치면서 생기는 공간이 존재한다.
=> 1칸 이동이 아닌 1칸 이동을 2번씩 진행해서 대각선 경로가 겹치는 부분도 노드로 체크
"""
from collections import defaultdict as dd
def solution(arrows):
    answer = 0
    d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    graph = dd(list)
    cur = (0, 0)
    for arrow in arrows:
        for _ in range(2):
            nxt = (cur[0] + d[arrow][0], cur[1] + d[arrow][1])
            if nxt in graph and cur not in graph[nxt]:
                answer += 1
            graph[cur].append(nxt)
            graph[nxt].append(cur)
            cur = nxt
    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))