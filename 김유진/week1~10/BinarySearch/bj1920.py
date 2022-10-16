import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

def binarySearch(target):
    low = 0
    high = len(arr)
    answer = 0
    while low <= high:
        middle = (low+high) // 2
        if middle > len(arr)-1:
            break
        if target == arr[middle]:
            answer =  1
            break
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return answer

for a in arr2:
    print(binarySearch(a))
