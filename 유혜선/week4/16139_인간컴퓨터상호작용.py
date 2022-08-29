"""
- 누적합

a: 0 - z: 25 
알파벳에 해당하는 인덱스에 (누적)개수를 저장하고
주어진 알파벳, 시작위치, 끝위치 에 맞는 개수를 출력
"""

import sys
input = sys.stdin.readline

string = input().rstrip()
acc = []

sub = [0] * 26
acc.append(sub)
for c in string:
    sub = sub[:]
    sub[ord(c)-97] += 1
    acc.append(sub)

print(*acc, sep='\n')
cnt = int(input())

for _ in range(cnt):
    c, i, j = input().split()
    print(acc[int(j)+1][ord(c)-97] - acc[int(i)][ord(c)-97])