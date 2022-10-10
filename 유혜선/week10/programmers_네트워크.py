"""
- 네트워크 (DFS/BFS)
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/43162
규칙 >
컴퓨터와 컴퓨터가 직,간접적으로 연결되어 있는 경우 같은 네트워크 상에 있다고 할 때,
네트워크의 개수를 구해라!

아이디어 >
1) DFS(with stack)를 이용해 연결된 네트워크 개수 찾기
2) Union Find 알고리즘 (예정)
3) BFS 이용 (예정)
"""
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                node = stack.pop()
                
                for k in range(n):
                    if k != node and computers[node][k] == 1 and not visited[k]:
                        visited[k] = True
                        stack.append(k)
            answer += 1
        if False not in visited:
            break
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1