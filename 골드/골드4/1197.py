import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
arr = []
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])
    
parent = [i for i in range(v + 1)]
arr.sort()
res = 0
for c, a, b in arr:
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += c

print(res)
'''
풀이
최소 스패닝 트리를 구하는 프로그램
스패닝 트리 = 신장 트리 = 사이클이 없이 모든 정점이 연결되어있는 그래프다
Union-Find를 사용하여 최소 스패닝 트리를 구한다
'''