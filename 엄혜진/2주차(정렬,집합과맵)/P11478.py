import sys

S = sys.stdin.readline().rstrip()

cases = []

for i in range(1, len(S) + 1):
    for j in range(0, len(S) - i + 1):
        cases.append(S[j:j+i])

sub_S = set(cases)

print(len(sub_S))