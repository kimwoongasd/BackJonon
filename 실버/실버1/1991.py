import sys
# 전위 순회
def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])
    
# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])

# 위 순회
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")


n = int(input())
# 사전을 활용하여 root를 key로 left, right를 value로 할당
# 위의 힌트로 풀수있었다
tree = {}
for i in range(n):
    root, lt, rt = sys.stdin.readline().strip().split()
    tree[root] = [lt, rt]

preorder("A")
print()
inorder("A")
print()
postorder("A")

# class Node:
#     def __init__(self, root, lt, rt):
#         self.root = root
#         self.lt = lt
#         self.rt = rt
        
# 전위 순회
# def preorder(root):
#     print(root, end="")
#     if tree[root].lt != ".":
#         preorder(tree[root].lt)
#     if tree[root].rt != ".":
#         preorder(tree[root].rt)
    
# 중위 순회
# def inorder(root):
#     if tree[root].lt != ".":
#         inorder(tree[root].lt)
#     print(root, end="")
#     if tree[root].rt != ".":
#         inorder(tree[root].rt)

# 위 순회
# def postorder(root):
#     if tree[root].lt != ".":
#         postorder(tree[root].lt)
#     if tree[root].rt != ".":
#         postorder(tree[root].rt)
#     print(root, end="")
# n = int(input())
# tree = {}
# for i in range(n):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = Node(root, left, right)
    
# preorder("A")
# print()
# inorder("A")
# print()
# postorder("A")