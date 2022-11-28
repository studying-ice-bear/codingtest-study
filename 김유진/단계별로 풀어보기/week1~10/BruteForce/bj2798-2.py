import sys
cnt, sum = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
result = 0
for i in range(cnt):
    for j in range(i+1, cnt):
        for k in range(j+1, cnt):
            if arr[i] + arr[j] + arr[k] > sum:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)