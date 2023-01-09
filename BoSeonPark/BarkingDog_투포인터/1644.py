import sys
import math
input = sys.stdin.readline

n = int(input())

def prime_list(n):
    sieve = [True] * (n + 1)
    
    m = int(math.sqrt(n))
    
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i] == True]


primes = prime_list(n)

s, e = 0, 0
length = len(primes)
r = 0
answer = 0

while True:
    
    if r == n:
        answer += 1
        
    if r > n:
        r -= primes[s]
        s += 1
    elif e == length:
        break
    elif r <= n:
        r += primes[e]
        e += 1

print(answer)