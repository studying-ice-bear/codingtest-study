import sys

input = sys.stdin.readline

N = int(input().rstrip())
paper = []
for _ in range(N):
    temp = list(map(int, input().rstrip().split()))
    paper.append(temp)

# print(N, paper)

answer = [0, 0, 0]


def travelsal(x, y, N):
    num = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if num != paper[i][j]:
                travelsal(x, y, N // 3)
                travelsal(x, y + (N // 3), N // 3)
                travelsal(x, y + (N // 3) * 2, N // 3)

                travelsal(x + (N // 3), y, N // 3)
                travelsal(x + (N // 3), y + (N // 3), N // 3)
                travelsal(x + (N // 3), y + (N // 3) * 2, N // 3)

                travelsal(x + (N // 3) * 2, y, N // 3)
                travelsal(x + (N // 3) * 2, y + (N // 3), N // 3)
                travelsal(x + (N // 3) * 2, y + (N // 3) * 2, N // 3)

                return 0

    answer[num] += 1


travelsal(0, 0, N)

print(answer[-1])
print(answer[0])
print(answer[1])

# python3: 68836KB	5144ms
# pypy3: 169880KB	1244ms