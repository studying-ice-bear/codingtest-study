import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

groupName = {}
teamName = {}

for _ in range(N):
    team = input().strip()
    num = int(input().strip())
    groupName[team] = []
    for i in range(num):
        member = input().strip()
        groupName[team].append(member)
        teamName[member] = team
    groupName[team].sort()


for _ in range(M):
    ss = input().strip()
    probType = int(input())

    if probType == 1:
        print(teamName[ss])
    else:
        print(*groupName[ss], sep='\n')
