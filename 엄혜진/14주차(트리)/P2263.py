import sys

sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline().rstrip())
inorder = list(map(int, sys.stdin.readline().rstrip().split()))
postorder = list(map(int, sys.stdin.readline().rstrip().split()))

tree = dict()

# 1. 시도
# 후위 순회에서 루트 노트 값만 얻고, 중위 순회에서 중간값을 재귀로 넘겨서 해결하려고 함
# 이렇게 해서는 답이 안 나오는 거 같다
#
# def apprehendTree(mid, end):
#     print(inorder[mid], end=' ')
#     apprehendTree(mid // 2 if mid % 2 == 0 else mid // 2 + 1, mid - 1)
#     apprehendTree(mid + ((end - mid) // 2) if mid % 2 == 0 else mid + ((end - mid) // 2 + 1), end)
#
# apprehendTree(inorder.index(postorder[-1]), n)

# 2. 158012KB	316ms
# 참조: https://velog.io/@bae_mung/Python-BOJ-2263-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%88%9C%ED%9A%8C
# 완전히 이해는 못한 느낌이다. 다시 꼭 풀어봐야하는 문제다.

position = [0] * (n + 1)
for i in range(n):
    position[inorder[i]] = i


def preorder(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return

    parent = postorder[post_e]
    print(parent, end=' ')

    left = position[parent] - in_s
    right = in_e - position[parent]

    preorder(in_s, in_s + left - 1, post_s, post_s + left - 1)
    preorder(in_e - right + 1, in_e, post_e - right, post_e - 1)


preorder(0, n - 1, 0, n - 1)
