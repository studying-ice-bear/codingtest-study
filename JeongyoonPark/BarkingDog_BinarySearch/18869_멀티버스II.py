m, n = map(int, input().split())
planet = []
result = 0

for _ in range(m):
    input_planet = list(map(int, input().split()))
    sorted_planet = sorted(list(set(input_planet)))

    dic = {sorted_planet[i] : i for i in range(len(sorted_planet))}

    temp = []
    for i in input_planet:
        temp.append(dic[i])
    planet.append(temp)

for i in range(m-1):
    for j in range(i+1,m):
        if planet[i] == planet[j]:
            result += 1

print(result)

'''
# 열~~심히는 한다! 버전
from itertools import combinations

m, n = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(m)]

print(planet)

def check(planet1, planet2):
    for i in combinations([i for i in range(n)],2):
        if planet1[i[0]] > planet1[i[1]] and planet2[i[0]] > planet2[i[1]]:
            continue
        if planet1[i[0]] < planet1[i[1]] and planet2[i[0]] < planet2[i[1]]:
            continue
        if planet1[i[0]] == planet1[i[1]] and planet2[i[0]] == planet2[i[1]]:
            continue
        return False
    return True

result = 0
for i in combinations([i for i in range(m)],2):
    if check(planet[i[0]], planet[i[1]]):
        result += 1
print(result)
'''
