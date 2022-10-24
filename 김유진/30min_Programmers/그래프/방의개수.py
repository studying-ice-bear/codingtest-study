from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x, y = 0, 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    for arrow in arrows:
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                answer += 1
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            elif (nx, ny) not in visit:
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            x, y = nx, ny

    return answer

def solution2(arrows):
    now = (0, 0)
    move = [(-1, 0), (-1, 1)]