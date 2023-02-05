import sys

na, nb = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
# print(na, nb, a, b)

answer = a - b
print(len(answer))
if len(answer) > 0:
    print(' '.join(map(str, sorted(answer))))
    # print(*(answer), answer) # 2 11 5 {2, 11, 5}

# -------------------------- 파이썬의 Asterisk (*) 의 용도 --------------------------
# 1. 곱셈 및 거듭제곱 연산
# print(2 * 3)
# print(2 ** 3)

# 2. 리스트형 컨테이너 타입의 데이터 반복 확장
# test_list = [0] * 10
# print(test_list) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# test_tuple = (0,) * 10
# print(test_tuple) # (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# 3. 가변인자 variadic parameters 사용

# positional arguments & keyword arguments
# def test_fuc(x, y, z=None, k=None):
#     print(x, y, z, k)

# test_fuc('hello', 'good') # hello good None None
# test_fuc('hello', 'good', z='bye') # hello good bye None
# test_fuc('hello', 'good', 'bye', k='world') # hello good bye world

# only positional arguments
# def pos_arg_fuc(*args):
#     print(args)

# pos_arg_fuc('hello', 'good', 'bye', 'world') # ('hello', 'good', 'bye', 'world')

# only keyword arguments
# def key_arg_fuc(**kwargs):
#     print(kwargs)

# positional arguments & keyword arguments
# def pos_key_arg_fuc(*args, **kwargs):
#     print(args)
#     print(kwargs)

# pos_key_arg_fuc('hello', 'good', 'bye', x='world', y='computer')
# ('hello', 'good', 'bye')
# {'x': 'world', 'y': 'computer'}

# key_arg_fuc(x='hello', y='good', z='bye', k='world') # {'x': 'hello', 'y': 'good', 'z': 'bye', 'k': 'world'}

# 4. 컨테이너 타입의 데이터를 언패킹
# test_list = [1, 2, 3, 4]
# print(test_list)  # [1, 2, 3, 4]
# print(*test_list)  # 1 2 3 4
# print(*(test_list))  # 1 2 3 4

# Ref: https://mingrammer.com/understanding-the-asterisk-of-python/
# ------------------------------------------------------------------------------
