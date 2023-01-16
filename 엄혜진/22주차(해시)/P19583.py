import sys


def split_time(t):
    h, m = map(int, t.split(':'))
    return (h, m)


S, E, Q = sys.stdin.readline().split()
S = split_time(S)
E = split_time(E)
Q = split_time(Q)


# print(S, E, Q)

def attandance_check(t, n):
    h, m = t

    if (h < S[0]) or (h == S[0] and m <= S[1]):
        accepted[n][0] += 1

    if (E[0] < h) or (E[0] == h and E[1] <= m):
        if (h < Q[0]) or (Q[0] == h and m <= Q[1]):
            accepted[n][1] += 1


accepted = {}
while True:
    try:
        time, nickname = sys.stdin.readline().split()
        time = split_time(time)

        if nickname not in accepted:
            accepted[nickname] = [0, 0]

        attandance_check(time, nickname)
    except:
        break

# print(accepted)
answer = 0
for i in accepted.keys():
    if accepted[i][0] >= 1 and accepted[i][1] >= 1:
        answer += 1
print(answer)
