import sys
input = sys.stdin.readline

n = int(input())
data = [int(x) for x in input().split()]
data.sort()
m = int(input())
m_list = [int(x) for x in input().split()]

def binary(data,i,start,end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if i < data[mid]:
        return binary(data,i,start,mid-1)
    elif i == data[mid]:
        return 1
    else:
        return binary(data,i,mid+1,end)

for i in m_list:
    start = 0
    end = n-1
    print(binary(data,i,start,end))