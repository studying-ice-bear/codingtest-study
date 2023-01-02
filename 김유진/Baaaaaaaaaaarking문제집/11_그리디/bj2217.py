import sys
N = int(sys.stdin.readline())
ropes = []
for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)
w = [0] * N

for i in range(1, N+1):
    w[i-1] = i * ropes[i-1]

print(max(w))

'''
문제 링크: https://www.acmicpc.net/problem/2217
문제 아이디어: https://pangsblog.tistory.com/21
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k만큼의 중량이 걸리게 된다.
-> (최대 중량이 작은 로프의 힘) * (로프 개수)

로프가 한 개일 때, 로프가 버틸 수 있는 한계가 최대 중량
로프가 두 개일 때, 두 개 중 가장 작은 로프의 최대 중량 * 2
로프가 세 개일 때, 세 개 중 가장 작은 로프의 최대 중량 * 3
.
.
.

'''