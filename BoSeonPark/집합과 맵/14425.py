import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

word_dict = {}
words = []
answer = 0
for _ in range(n):
    word_dict[input().strip()] = 1

for _ in range(m):
    words.append(input().strip())

for word in words:
    if word in word_dict:
        answer += 1

print(answer)

"""
풀이
n개의 문자를 dictionary로 만든다
m개의 문자는 list에 저장
m개의 문자가 저장된 list를 반복문으로 하나씩 접근해 dictionary에 있는지 확인
"""