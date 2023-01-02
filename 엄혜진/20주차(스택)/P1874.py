import sys

n = int(sys.stdin.readline().rstrip())

answer = []
stack = []
next_n = 1
has_answer = True

for _ in range(n):
    cur = int(sys.stdin.readline().rstrip())
    while next_n <= cur:
        stack.append(next_n)
        next_n += 1
        answer.append('+')

    if stack[-1] == cur:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        has_answer = False
        break

if has_answer:
    print('\n'.join(answer))


# # # 문제 이해하는게 어려웠다 ㅋㅋㅋㅋ
#
# n = int(input().rstrip())
# nums = [i for i in range(n, 0, -1)]
# # print(nums)
# stack = [0]
# answer = []
# for i in range(1, n + 1):
#     new = int(input().rstrip())
#     top = stack[-1]
#     # print(new, stack, nums)
#
#     if top == new:
#         stack.pop()
#         answer.append('-')
#     else:
#         while top != new:
#             if top < new:
#                 stack.append(nums.pop())
#                 answer.append('+')
#             else:
#                 answer = ['NO']
#                 break
#             top = stack[-1]
#         stack.pop()
#         answer.append('-')
#
# for i in answer:
#     print(i)
#
# # 어제는 너무 하기 싫었다... 핀트 잘못잡으니까 시간도 너무 오래 걸려서 지쳤다. 새로운 마음으로 다시 풀기!
#
