import sys
N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))
meetings.sort(key=lambda x: x[0])
print(meetings)
meetings.sort(key=lambda x: x[1])
print(meetings)

cnt = 1
end = meetings[0][1]
for i in range(1, N):
    if meetings[i][0] >= end:
        cnt += 1
        end = meetings[i][1]

print(cnt)

'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

output:
4
'''