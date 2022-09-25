"""
- 분할 정복

idea> 거듭제곱 빨리 풀기와 비슷
- 문제 해결방법 자체는 어렵지 않음
- A^k = A^(k//2) * A^(k//2)  (k = 짝수)
- A^k = A^(k//2) * A^(k//2) * A (k = 홀수)

⭐ 숫자가 엄청 커지므로 전체 계산 후 print할때 1000으로 나눠주면 시간초과 ㅠㅠ
=> 계산할 때 계속 1000으로 나눠줘야 함
=> 모듈러 연산의 속성으로 나누고 계산해도 괜찮음
=> 😵 

⭐⭐ 모듈러 연산
1. (a + b) mod n = ((a mod n) + (b mod n)) mod n
2. (a - b) mod n = ((a mod n) - (b mod n)) mod n
3. (a * b) mod n = ((a mod n) * (b mod n)) mod n
출처: https://www.crocus.co.kr/1231 [Crocus:티스토리]


"""
import sys
input = sys.stdin.readline

n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


# a = 2차원 배열일때
# b = list(zip(*a))
# b는 a의 전치 행렬이 된다. 
def multiple(m1, m2):
    m2_tr = list(zip(*m2))
    return [[sum(a*b for a, b in zip(row, col)) % 1000 for col in m2_tr] for row in m1]


def dp(b):
    global matrix
    if b == 1:
        # 1일때 그냥 matrix를 리턴해줬는데
        # 요소가 1000이 넘어갈 수 있으므로 1000으로 나눈후 리턴
        # 요게 틀리면 80% 정도에서 틀렸다고 나옴
        return [[x % 1000 for x in row] for row in matrix]
    
    if b == 2:
        return multiple(matrix, matrix)
    
    prev = dp(b // 2)
    answer = multiple(prev, prev)

    if b % 2 == 1:
        answer = multiple(answer, matrix)
    
    return answer
        
        
answer = dp(b)

for c in range(n):
    print(*answer[c])
