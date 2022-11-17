import sys
first = [""]+list(sys.stdin.readline().rstrip())
second = [""]+list(sys.stdin.readline().rstrip())
lcs = [[""]*len(second) for _ in range(len(first))]

for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]:
            lcs[i][j] = lcs[i-1][j-1] + first[i]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]

print(len(lcs[-1][-1]), lcs[-1][-1], sep="\n")