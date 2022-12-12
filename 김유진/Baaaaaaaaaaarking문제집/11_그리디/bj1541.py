import sys
s = sys.stdin.readline().strip()
arr = []
start = 0
for i in range(len(s)):
    if s[i] == '+':
        arr.append(s[i].split('+'))
    elif s[i] == '-':
        arr.append(s[i].split('-'))
        arr.append(s[start:i])
        start = i

print(arr)
'''
문제 링크: https://www.acmicpc.net/problem/1541
'''