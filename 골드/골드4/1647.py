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

n, m = map(int, input().split())
arr = []
for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])

arr.sort()
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

res = 0
max_cost = 0

for c, a, b in arr:
    if find_parent(a) != find_parent(b):
        union(a, b)
        res += c
        max_cost = max(max_cost, c)

print(res - max_cost)

'''
풀이
최소 신장트리를 찾는 크루스칼 알고리즘

크루스칼 알고리즘으로 최소 스패닝 트리를 만들고 여기서 비용이 가장 큰 간선을 잘라주면 된다.
최소 스패닝 트리에서는 사이클이 존재하지 않는다.
그렇기 때문에 여기서 간선 하나만 잘라주면 두 개의 스패닝 트리가 만들어진다.

크루스칼 알고리즘을 처음 본다
크루스칼에 대한 알고리즘을 공부해야겠다.
'''