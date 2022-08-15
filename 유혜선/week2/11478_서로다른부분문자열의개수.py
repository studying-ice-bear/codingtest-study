"""
- 이중 for문으로 abcde 의 경우 
a , ab, abc, abcd, abcde
b, bc, bcd, bcde
c, cd, cde
d, de
e
위 요소들을 리스트에 넣은 후 set으로 중복 제거

"""
import sys

input = sys.stdin.readline

string = input()
arr = []

for i in range(len(string)-1):
    for j in range(i+1, len(string)):
        sub = string[i:j]
        arr.append(sub)

print(len(set(arr)))
