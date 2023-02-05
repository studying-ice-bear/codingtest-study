import sys
input = sys.stdin.readline

k, n = map(int,input().split())
data = [int(input()) for _ in range(k)]

def binary_search(data,start,end):
    mid = (start+end)//2
    count = 0
    if start > end:
        return end
    for i in data:
        count += i // mid
    if count >= n:
        return binary_search(data,mid+1,end)
    else:
        return binary_search(data,start,mid-1)

start = 1
end = max(data)
print(binary_search(data,start,end))