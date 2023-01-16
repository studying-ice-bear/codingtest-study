import sys
input = sys.stdin.readline

k, l = map(int, input().split())
system = {}

for i in range(l):
    number = input().strip()
    system[number] = i

result = sorted(system.items(), key=lambda x: x[1])
if len(result) < k: k = len(result)

for j in range(k):
    print(result[j][0])

'''
런타임 에러 (IndexError)에 대한 반례

2 3
20140101
20140101
20140101


답

20140101
'''