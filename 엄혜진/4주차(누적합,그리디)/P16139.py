import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline().rstrip())

dp = {}
for _ in range(q):
    alphabet, l, r = sys.stdin.readline().rstrip().split()
    l = int(l)
    r = int(r)
    if alphabet not in dp:
        dp_temp = [0]
        temp = 0
        for i in range(len(S)):
            if S[i] == alphabet:
                temp += 1
                dp_temp.append(temp)
            else:
                dp_temp.append(temp)
        dp[alphabet] = dp_temp
        # print(dp[alphabet])
    sys.stdout.write(str(dp[alphabet][r + 1] - dp[alphabet][l]) + '\n')

# python3으로 채점하니까 50점이었는데 Pypy3으로 채점하니 100점!
