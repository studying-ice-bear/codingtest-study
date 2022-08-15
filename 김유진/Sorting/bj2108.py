import sys
numTestcase = int(sys.stdin.readline())
arr = []
for _ in range(numTestcase):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

'''
    산술평균 : N개의 수들의 합을 N으로 나눈 값
    중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    최빈값 : N개의 수들 중 가장 많이 나타나는 값
    범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''

a_mean = round(sum(arr) / numTestcase)  # 산술 평균
mid = arr[int(numTestcase/2)]   # 중앙값
print(a_mean)
print(mid)

# 최빈값
# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

check = {}
for a in arr:
    if a not in check.keys():
        check[a] = 1
    else:
        check[a] += 1
# print("check", check)

mode_dic = {}
for i in sorted(check.values(), reverse=True):
    for k in check.keys():
        if check[k] == i:
            mode_dic[k] = check[k]
# print("mode_dic", mode_dic)

if len(mode_dic) == 1:
    print(list(mode_dic.keys())[0])
else:
    if mode_dic[list(mode_dic.keys())[0]] == mode_dic[list(mode_dic.keys())[1]]:
        print(list(mode_dic.keys())[1])
    else:
        print(list(mode_dic.keys())[0])

# 범위
num_range = arr[-1] - arr[0]
print(num_range)