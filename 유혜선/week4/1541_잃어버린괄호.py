"""
- 그리디

idea > 식의 최솟값을 만들기 위해서는 최대한 많은 수를 빼야함
=> 첫번째 "-"가 등장한 이후의 숫자들을 모두 빼면 최솟값을 만들 수 있음
"""
import sys
input = sys.stdin.readline

f = input()

val = ""
total = 0
for i in range(len(f)):
    if val and val[0] == "-" and f[i] in "+-":
        total += int(val)
        val = "-"

    elif f[i] in "+-":
        total += int(val)
        val = f[i]
        
    else:
        val += f[i]

total += int(val)
print(total)