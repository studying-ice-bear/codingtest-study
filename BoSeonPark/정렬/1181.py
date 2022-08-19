import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())
  
words = sorted(list(set(words)), key=lambda x: (len(x), x))

for word in words:
    print(word)
    
"""
풀이
sorted(key=lambda)를 사용해 조건을 여러개 추가해 한 번에 정렬
"""