import sys

k, l = map(int, sys.stdin.readline().split())
log = {}
for i in range(l):
    num = sys.stdin.readline().rstrip()
    log[num] = i

sorted_log = sorted(log.items(), key=lambda item: item[1])
# print(sorted_log)

for j in range(min(k, len(sorted_log))):
    print(sorted_log[j][0])

# [ 여러 정답 코드에서 발견한, 처음 본 메소드 ]
# print(dict.fromkeys(reversed(log)))
# dict.fromkeys(seq, value)
# 공식문서: https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
# 설명: 딕셔너리의 키값으로 새로운 딕셔너리를 만드는 메소드. value 값을 설정하지 않으면 None으로 설정된다.