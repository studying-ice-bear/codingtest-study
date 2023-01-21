import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int,input().split()))

def binary_search(data,start,end):
    cnt = 0
    mid = (start+end)//2
    if start > end:
        return end
    for i in trees:
        if i > mid:
            cnt += (i-mid)
    if cnt >= m:
        return binary_search(data,mid+1,end)
    else:
        return binary_search(data,start,mid-1)

start = 0
end = max(trees)
print(binary_search(trees,start,end))