import sys
N = int(sys.stdin.readline())
answer = 0
two = [0] * 1000001
two[0] = 0
two[1] = 1
two[2] = 2

for i in range(3, N+1):
    two[i] = two[i-2] + two[i-1]
    two[i] = 15746

print(answer)


'''
00 타일, 1 타일
'''
# 첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.

# 0이 오는 경우, 다음 자릿 수는 0으로 확정
# 1이 오는 경우,
# 0 or 1
# 0: 자릿 수가 2이상 남을 때
# 1: 남은 자릿 수가 1이면 1로 확정
