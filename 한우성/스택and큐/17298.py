import sys

n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
answer = []
for i in range(n):
    temp2 = temp[i+1:]
    if temp2 == []:
        answer.append(-1)
        break
    temp3 = list(filter(lambda x: x>temp[i], temp2))
    if temp3 == []:
        answer.append(-1)
    else:
        answer.append(temp3[0])

print(answer)