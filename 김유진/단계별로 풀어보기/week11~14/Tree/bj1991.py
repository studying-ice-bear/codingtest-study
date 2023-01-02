import sys
N = int(sys.stdin.readline())   # 이진 트리 노드의 개수

tree = {}
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != ".":
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.root = data
#
# tree = [Node for _ in range(N)]
#
#
# # 노드, 왼쪽 자식 노드, 오른쪽 자식
# for i in range(N):
#     node, left, right = sys.stdin.readline().split()
#     tree[i].root = node
#     tree[i].left = left
#     tree[i].right = right
#
# def preorder(data):
#     if data.root != ".":
#         print(data.root)
#         preorder(data.left)
#         preorder(data.right)
#
# preorder(tree)