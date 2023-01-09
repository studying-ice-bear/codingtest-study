"""
- LCS(Longest Common Subsequence)

idea> 동적계획법?!
- table[i][j] 를 비교할 때(a 문자열의 i번째, b 문자열의 j번째 글자 비교)
- 글자가 같으면 해당 글자 전 문자열의 LCS 개수 + 1
- 글자가 다르면 table[i-1][j], table[i][j-1] 중에 최댓값 
(a 문자열의 i-1번째까지와 b 문자열의 j까지 비교, a 문자열의 i번째까지와 b 문자열의 j-1까지 비교)
"""
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

l1 = len(s1)
l2 = len(s2)

table = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if s1[i-1] == s2[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

answer = []
i = l1
j = l2
val = table[i][j]
while True:
    if table[i][j] == 0 or i == 0 or j == 0:
        break

    elif table[i-1][j] == val:
        i -= 1
    elif table[i][j-1] == val:
        j -= 1
    else:
        answer.append(s1[i-1])
        i -= 1
        j -= 1
        val -= 1

answer = answer[::-1]
print(len(answer))
print(''.join(answer))
