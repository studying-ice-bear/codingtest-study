import sys
input = sys.stdin.readline

words = input().strip()
length = len(words)
word_dict = {}
for i in range(length):
    for j in range(i + 1, length+1):
        word_dict[words[i:j]] = 1

print(len(word_dict.keys()))

"""
풀이
문자 하나씩 순서대로 접근해 해당 문자 기준으로 마지막 문자까지 하나씩 추가해 key로 사용해 dictionary로 만든다
중복되는 문자열이 나올 수 있지만 word_dict[words[i:j]] = 1로 하기 때문에 상관없음
"""