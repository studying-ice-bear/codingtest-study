import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

dic = {}
nums = list(sorted(set(arr)))

for i in range(len(nums)):
    dic[nums[i]] = i

for j in arr:
    print(dic[j], end=' ')

'''
다른 풀이:
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))

시도1:
answer = [0] * len(arr)
at, to = 0, 0

while at < len(arr):
    if to == len(arr):
        to = at
        at += 1

    else:
        if arr[at] > arr[to]:
            answer[at] += 1
        to += 1

print(*answer, sep=' ')

반례:
    6
    1000 999 1000 999 1000 999
    
    output:
    3 0 3 0 2 0
    
    answer:
    1 0 1 0 1 0
'''