import itertools
import math
import sys

N = int(sys.stdin.readline().rstrip())

synergy = [0] * N
for i in range(N):
    synergy[i] = list(map(int, sys.stdin.readline().rstrip().split()))
# print(synergy)

teams = list(itertools.combinations(range(N), N//2))
# print(teams)

answer = math.inf
for k in range(len(teams) // 2):
    a_chemi = 0
    b_chemi = 0
    for (i, j), (h, g) in zip(list(itertools.combinations(teams[k], 2)), list(itertools.combinations(teams[len(teams) - k - 1], 2))):
        # print((i, j), (h, g))
        a_chemi += synergy[i][j] + synergy[j][i]
        b_chemi += synergy[h][g] + synergy[g][h]
    # print(a_chemi, b_chemi, abs(a_chemi - b_chemi))
    answer = min(answer, abs(a_chemi - b_chemi))

sys.stdout.write(str(answer))