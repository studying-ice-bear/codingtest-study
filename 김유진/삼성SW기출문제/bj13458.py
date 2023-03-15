import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

answer = 0
for a in arr:
    answer += 1
    if a-B > 0:
        answer += (a - B) // C

        if (a - B) % C > 0:
            answer += 1

print(answer)
