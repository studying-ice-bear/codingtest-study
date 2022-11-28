import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (k + 1)
dp[0] = 1

for i in coin:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])

# 모르겠어서 검색함

# 여기부터 코드 설명:
# 각 코인의 최대 개수를 구해서 dp에 저장하는거 같다.
# i가 j의 값을 채울 수 있으면 값을 더한다. j // i > 0이면 j코인으로 값을 채울 수 있으니까?
# 솔직히 이해를 못했다.. 이게 뭔소리고... 이런 생각을 어떻게 하냐...
