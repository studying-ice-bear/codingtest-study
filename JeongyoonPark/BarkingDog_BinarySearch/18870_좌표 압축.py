n = int(input())
x = list(map(int, input().split()))

new_x = sorted(list(set(x)))
# dic = {}
# for i in range(len(new_x)):
#     dic[new_x[i]] = i
dic = {new_x[i] : i for i in range(len(new_x))}

result = []
for j in x:
    result.append(dic[j])

print(*result)