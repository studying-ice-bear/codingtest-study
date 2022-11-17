import sys

n = int(sys.stdin.readline().rstrip())
tree = dict()
for _ in range(n):
    p, c_l, c_r = sys.stdin.readline().rstrip().split()
    tree[p] = [c_l, c_r]


# 전위 순회
def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


# 중위 순회
def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


# 후위 순회
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

# 30840KB	68ms
