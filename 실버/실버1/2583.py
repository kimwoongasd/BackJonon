# bfs
from collections import deque
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    count = 1
    while dq:
        a, b = dq.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
                arr[xx][yy] = -1
                count += 1
                dq.append((xx, yy))
    return count
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for i in range(y_1, y_2):
        for j in range(x_1, x_2):
            arr[i][j] = 1
area = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            t = bfs(i, j)
            area.append(t)
            
print(len(area))
area.sort()
print(*area)

# dfs
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y):
#     global count
#     arr[x][y] = -1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
#             count += 1
#             dfs(xx, yy)

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# m, n, k = map(int, input().split())
# arr = [[0] * n for _ in range(m)]
# for _ in range(k):
#     x_1, y_1, x_2, y_2 = map(int, input().split())
#     for i in range(y_1, y_2):
#         for j in range(x_1, x_2):
#             arr[i][j] = 1

# area = []
# for i in range(m):
#     for j in range(n):
#         if arr[i][j] == 0:
#             count = 1
#             dfs(i, j)
#             area.append(count)
# print(len(area))
# area.sort()
# print(*area)