import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(x):
    for y in arr[x]:
        if ch[y] == 0:
            ch[y] = x
            dfs(y)

n = int(input())

arr = [[] for _ in range(n + 1)]
for i in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
ch = [0] * (n + 1)
dfs(1)
for x in range(2, n + 1):
    print(ch[x])

# dq = deque()
# dq.append(1)

# while dq:
#     node = dq.popleft()
#     for x in arr[node]:
#         if ch[x] == 0:
#             ch[x] = node
#             dq.append(x)
# for x in range(2, n + 1):
#     print(ch[x])