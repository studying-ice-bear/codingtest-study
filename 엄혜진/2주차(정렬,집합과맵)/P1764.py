import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

not_listen = {}

for _ in range(N):
    not_listen[sys.stdin.readline().rstrip()] = True

nothings = []

for i in range(M):
    not_see = sys.stdin.readline().rstrip()
    if not_listen.get(not_see) != None:
        nothings.append(not_see)

nothings.sort()

sys.stdout.write(str(len(nothings)) + '\n')
for nothing in nothings:
    sys.stdout.write(nothing + '\n')

# 다른 방법: 자료구조 set 이용
# Doc: https://docs.python.org/3/library/stdtypes.html?highlight=set#set

# 코드
# import sys
# n, m = map(int, input().split())
# nameList = sys.stdin.read().splitlines() # 여러줄 입력 받는 것도 처음 봄!
# hearset = set(nameList[:n]) # 리스트를 바로 셋으로 변환할 수 있다!
# seeset = set(nameList[n:])
# ret = list(hearset & seeset) # & 로 교집합
# ret.sort()
# print(len(ret))
# for i in ret:
#     print(i)
