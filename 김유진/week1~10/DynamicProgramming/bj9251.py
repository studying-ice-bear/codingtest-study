import sys
string1 = sys.stdin.readline()
string2 = sys.stdin.readline()
arr1 = []
for s in string1:
    if s == '\n':
        continue
    arr1.append(s)

arr2 = []
for s in string2:
    if s == '\n':
        continue
    arr2.append(s)

print(arr1)
print(arr2)
N = len(arr1)
M = len(arr2)
lcs = [[0] * (N+1) for _ in range(M+1)]
print(lcs)

for i in range(1, N+1):
    for j in range(1, M+1):
        if arr1[i-1] == arr2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs)
print(lcs[-1][-1])
'''
ACAYKP
CAPCAK
output:
4

ACA
CAPCAK
X
'''