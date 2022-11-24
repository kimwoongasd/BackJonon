from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(int, input()))
    arr.append(a)

dq = deque()
dq.append((0, 0))
ch = [[0] * m for _ in range(n)]
while dq:
    x, y = dq.popleft()
    
    for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0 and arr[xx][yy] == 1:
                dq.append((xx, yy))
                ch[xx][yy] = ch[x][y] + 1
print(ch[n - 1][m - 1] + 1)

        

# 깊이우선 탐색 시간초과
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y, c):
#     global res
#     if x == n - 1 and y == m - 1:
#         if c < res:
#             res = c
    
#     else:
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0 and arr[xx][yy] == 1:
#                 ch[xx][yy] = 1
#                 dfs(xx, yy, c + 1)
#                 ch[xx][yy] = 0


# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     a = list(map(int, input()))
#     arr.append(a)

# ch = [[0] * m for _ in range(n)]
# ch[0][0] = 1
# res = 2147000000
# dfs(0, 0, 1)
# print(res)