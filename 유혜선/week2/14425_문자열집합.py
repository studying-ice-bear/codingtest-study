"""
- sys.stdin.readline을 사용하면 훨씬 빠름
- 단어를 담는 집합은 set, dict 다 상관없음
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = {input().rstrip(): True for _ in range(n)}
answer = 0

for _ in range(m):
    word = input().rstrip()
    if word in words:
        answer += 1

print(answer)