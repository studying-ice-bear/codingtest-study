import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

idx_dict = {}
name_dict = {}
problem = []

for i in range(n):
    poketmon = input().strip()
    name_dict[poketmon] = i + 1
    idx_dict[str(i+1)] = poketmon

for _ in range(m):
    problem.append(input().strip())

for p in problem:
    if p in idx_dict:
        print(idx_dict[p])
        continue
    elif p in name_dict:
        print(name_dict[p])
        continue

"""
풀이
n 개의 포켓몬이름에 대해 index:poketmon_name, poketmon_name:index 형태의 두 개의 dictionary를 생성
m개의 문제에 대해 반복문으로 한 개씩 접근해 두 개의 dictionary에 key로 존재하는지 확인하고 존재하면 해당 key 값을 출력
"""