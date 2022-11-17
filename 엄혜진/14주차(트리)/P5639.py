import sys

sys.setrecursionlimit(10 ** 9)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline().rstrip()))
    except:
        break


# print(preorder)

def postorder(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(preorder[start])


postorder(0, len(preorder) - 1)

# 참조: https://imzzan.tistory.com/41
# 이해는 됐는데 작동방식을 그대로 구현할 수 있을지 모르겠다. 꼭 다시 풀어봐야 하는 문제!
