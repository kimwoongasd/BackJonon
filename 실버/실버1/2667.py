# bfs
from collections import deque
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    count = 1
    while dq:
        a ,b = dq.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 1:
                arr[xx][yy] = 0
                count += 1
                dq.append((xx, yy))
                
    return count

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n = int(input())
arr = []
for _ in range(n):
    a = list(map(int, input()))
    arr.append(a)

res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr[i][j] = 0
            count = bfs(i, j)
            res.append(count)
res.sort()
print(len(res))
for x in res:
    print(x)

# dfs
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y):
#     global count
#     arr[x][y] = 0
#     count += 1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 1:
#             dfs(xx, yy)

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# n = int(input())
# arr = []
# for _ in range(n):
#     a = list(map(int, input()))
#     arr.append(a)

# res = []
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             count = 0
#             dfs(i, j)
#             res.append(count)
# res.sort()
# print(len(res))
# for x in res:
#     print(x)
