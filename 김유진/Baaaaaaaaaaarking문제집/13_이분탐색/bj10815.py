import sys
input = sys.stdin.readline
N = int(input())
nn = sorted(list(map(int, input().strip().split())))
M = int(input())
mm = list(map(int, input().strip().split()))

# 이분 탐색을 활용한 풀이(1848ms)
def bs(x):
    low, high = 0, len(nn) - 1
    exist = 0

    while low <= high:
        mid = (low+high) // 2
        if nn[mid] < x:
            low = mid + 1
        elif nn[mid] > x:
            high = mid - 1
        else:
            exist = 1
            break

    return exist

for m in mm:
    print(bs(m), end=' ')

'''
# 딕셔너리를 활용한 풀이(888ms)
answer = {}
for n in nn:
    answer[n] = 1
for m in mm:
    if m not in answer.keys():
        print(0, end=' ')
    else:
        print(1, end=' ')


# 한 줄 풀이
print(' '.join("1" if x in nn else "0" for x in mm))

테스트케이스
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''