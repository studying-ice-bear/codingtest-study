import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

left = {}
right = []
answer = []
for _ in range(n):
    name = input().strip()
    left[name] = left.get(name, 0) + 1

for _ in range(m):
    right.append(input().strip())

for r in right:
    if left.get(r, 0) != 0:
        answer.append(r)

print(len(answer))
answer.sort()
for a in answer:
    print(a)

"""
n개는 dictionary로
m개는 list로 저장
list에 저장된 이름을 반복문을 통해 하나씩 가져와 key로 사용해 dictionary에
해당 key가 있는지 확인
존재하면 answer에 추가, 없으면 continue
마지막에 answer list를 한 번 sort해주고 출력
"""