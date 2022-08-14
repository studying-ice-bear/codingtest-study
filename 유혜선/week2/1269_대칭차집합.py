"""
- 대칭차집합은 (A - B) + (B - A) => (A ∪ B) - (A ∩ B)
- 개수만 구하면 되므로 (합집합의 원소 개수) * 2에서 각 집합의 원소 개수를 빼기

A + B = (A ∪ B) + (A ∩ B) 

(A ∪ B) * 2 - (A + B) 
= (A ∪ B) * 2 - ((A ∪ B) + (A ∩ B))
= (A ∪ B) - (A ∩ B)
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(2):
    arr += list(map(int, input().split()))

common = len(set(arr))

print(common * 2 - (n + m))