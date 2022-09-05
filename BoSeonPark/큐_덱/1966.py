import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    docs = deque(list(map(int, input().split(' '))))
    docs_index = deque([i for i in range(n)])
    count = 0
    
    while True:
        if docs[0] == max(docs):
            count += 1
            if docs_index[0] == m:
                print(count)
                break
            else:
                docs.popleft()
                docs_index.popleft()
        else:
            docs.append(docs.popleft())
            docs_index.append(docs_index.popleft())