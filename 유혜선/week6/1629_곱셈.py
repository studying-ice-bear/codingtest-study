"""
- 분할 정복

idea> 모듈러 법칙
- k = i + j 일때
=> A^k mod B = (A^i * A^j) mod B = (A^i mod B * A^j mod B) mod B

"""
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# sol1.
# def dnc(t, c, d):
#     if c == 0:
#         return 1

#     elif c == 1:
#         return t % d
    
#     elif c % 2 == 0:
#         return dnc(t, c//2, d) ** 2 % d
    
#     else:
#         return dnc(t, c//2, d) ** 2 * t % d


# print(dnc(a, b, c))

# sol2.
# def speed_modular_calc(t, c, d):
#     if c < 2:
#         return t ** c % d
    
#     else:
#         return speed_modular_calc(t, c//2, d) ** 2 % d


# binary_b = bin(b)

# binary_b_r = binary_b[::-1]

# answer = 1
# for idx, bb in enumerate(binary_b_r):
#     if bb == 'b':
#         break

#     elif bb == '0':
#         continue

#     else:
#         answer *= speed_modular_calc(a, 2**idx, c)

# print(answer % c)