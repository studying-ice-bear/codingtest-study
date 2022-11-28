import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * (n + 1)
for i in range(n):
    temp = []
    for j in range(i):
        if a[j] < a[i]:
            temp.append(dp[j])
    if not temp:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + max(temp)

print(max(dp))

# 모르겠어서 검색함. 담에는 꼭 내 힘으로 풀 수 있길!

# 여기부터 코드 설명:
# dp는 i까지의 증가수열의 합을 저장한 것이다.
# dp[i]에 들어갈 원소는 a[0:i] 중에 a[i] 보다 작은 원소여야 한다. 그래야 증가 수열이 되니까.
# 그래서 0부터 i-1번 원소까지 i번째 원소보다 작은 원소가 있으면 임시 배열에 저장한다.
# 다 순환한 후에, 임시 배열에 원소가 있으면, 최대 증가수열이 될 수 있다는 거다.
# dp는 증가수열의 합을 저장하는 거니까 임시 배열의 총 합 + a[i]를 합해서 저장한다.
# 만약 임시배열에 원소가 없다면, 0 ~ i-1번 원소 중에 i번째 원소보다 작은 것은 없으므로 i 번째 원소가 수열의 첫번째가 된다.
# 그러므로 dp에 i 번째 원소를 그대로 저장한다.
