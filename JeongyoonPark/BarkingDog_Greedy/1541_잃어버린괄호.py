problem = input()
num = ''
number = []
result = []

for i in problem:
    if i == "-" or i == "+":
        number.append(num)
        num = ''
        number.append(i)
    else:
        num += i
number.append(num)

result = 0
flag = False
for i in number:
    if i == '-':
        flag = True
    elif i == '+':
        continue
    else:
        if flag:
            result -= int(i)
        else:
            result += int(i)  
print(result)