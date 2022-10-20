"""
- 투 포인터

idea> 부분합 체크!
- 두개의 포인터는 맨 처음부터 시작한다! 어차피 배열 끝까지 탐색해야되므로 end포인터(p2)는 for문으로 해줌
- 차례대로 sub_total을 구해준 후, sub_total == n이 되는 경우 answer += 1
- 그 외 로직은 부분합과 동일

메모리, 시간 >
※ 소수 구하는 부분에서 dict 자료형(소수 아닌것들 삭제하면서) 사용했을 때: 메모리 초과
✅ list 자료형(T/F 구분) 사용했을 때(주석): 메모리: 72540KB   시간: 1524ms
✅ list 자료형(T/F 구분) 사용하고 슬라이싱 변환한 경우(현재 코드): 메모리: 93344KB 시간: 440ms
"""
import sys
input = sys.stdin.readline

def prime_number(n):
    dic = [True] * (n+1)
    dic[0], dic[1] = False, False

    for p in range(2, int(n ** 0.5) + 1):
        if dic[p]:
            # k = 2
            # while p * k <= n:
            #     dic[p*k] = False
            #     k += 1
            dic[p*2::p] = [False] * (n // p - 1)
    return [idx for idx, val in enumerate(dic) if val]

def solution(n):
    if n == 1:
        print(0)
        return

    primes = prime_number(n)
    l = len(primes)
    p1 = 0
    sub_total = 0
    answer = 0
    for p2 in range(l):
        sub_total += primes[p2]

        while sub_total > n and p1 <= p2:
            sub_total -= primes[p1]
            p1 += 1
        
        if sub_total == n:
            answer += 1
    print(answer)

n = int(input())
solution(n)

