from itertools import combinations

for _ in range(int(input())):
    dict = {}
    n = int(input())
    for j in range(n):
        name, type = input().split()
        if type in dict.keys():
            dict[type].append(name)
        else:
            dict[type] = [name] 

    # print(dict)
    '''
    1가지 고르는 경우는 무조건 n개
    2가지 옷 종류 구하고 그 옷의 value 값 개수를 곱해주고
    3가지 //

    result = n
    type_key = dict.keys()
    for i in range(2, len(type_key)+1):
        temp = 1
        for j in combinations(type_key, i):
            print(j)
    '''
    result = 1
    type_key = dict.keys()
    for k in type_key:
        # 0인 경우도 포함해서 (각각의 경우를 곱함)
        result *= (len(dict[k])+1)
    # (0,0,0 ...) 모두 0인 경우는 빼야함
    print(result-1)


# key 하나 당 입지 않거나 한 가지 제품만 착용 가능하다. {0,1}
# 이때 전체 0은 안됨.
# 종류 당 한 개를 두 가지 종류를 고를 땐 경우의 수가 n(A) X n(B)

