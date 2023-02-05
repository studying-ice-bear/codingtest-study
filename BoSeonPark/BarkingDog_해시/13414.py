import sys
input = sys.stdin.readline

k, l = map(int, input().split())
cnt = 0
waiting = dict()

for _ in range(l):
    num = input().strip()
    
    if num not in waiting:
        cnt += 1
        waiting[num] = cnt
    else:
        cnt += 1
        waiting[num] = cnt
        
result = [[k, v] for k, v in waiting.items()]
result.sort(key=lambda x : x[1])
for id, _ in result[:k]:
    print(id)