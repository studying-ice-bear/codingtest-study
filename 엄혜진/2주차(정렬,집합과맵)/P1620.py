import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pocketmon_num = {}
num_pocketmon = {}
for i in range(N):
    pocketmon = sys.stdin.readline().rstrip()
    idx = str(i + 1)
    pocketmon_num[pocketmon] = idx
    num_pocketmon[idx] = pocketmon

quests = []
for _ in range(M):
    quests.append(input())

for quest in quests:
    if quest.isnumeric():
        sys.stdout.write(num_pocketmon[quest] + '\n')
    else:
        sys.stdout.write(pocketmon_num.get(quest) + '\n')
# 파이썬 숫자 판별법
# Reference: https://www.delftstack.com/ko/howto/python/python-check-if-character-is-number/
# 1. if-else 문
# 2. str.isdigit(): 문자열의 모든 문자가 숫자인 경우 True 반환
# 3. str.isnumeric(): 문자열의 모든 문자가 숫자인 경우 True 반환. 음수나 소수는 숫자라고 간주되지 않음

# 시간 초과가 난다....
# 검색해보니 빠른 입력을 추천한다고 한다...
# sys 입력을 생활화 하자..