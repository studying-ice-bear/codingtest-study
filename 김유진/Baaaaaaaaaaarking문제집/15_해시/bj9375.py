import sys

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    clothNum = int(sys.stdin.readline())
    cloths = {}

    for i in range(clothNum):
        cloth, kind = sys.stdin.readline().strip().split(' ')
        if kind not in cloths.keys():
            cloths[kind] = [0, cloth]
        else:
            cloths[kind].append(cloth)

    total = 1
    for i, j in cloths.items():
        total *= len(j)

    print(total-1)

'''
문제 링크: https://www.acmicpc.net/problem/9375
- 다른 풀이: 개수를 저장하기 (https://www.acmicpc.net/source/53157187)
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = {}
    gearnum = int(input())
    cnt = 1

    for _ in range(gearnum):
        _, gear = input().split()
        if gear in arr:
            arr[gear] += 1
        else:
            arr[gear] = 1

    for i in arr.items():
        cnt = cnt * (i[1]+1)
    print(cnt-1)
'''