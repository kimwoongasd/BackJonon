# bfs 풀이
import sys 
sys.setrecursionlimit(10000) 
from collections import deque

def bfs(a, b):
    q = deque([(a, b)])
    ch[a][b] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if ch[xx][yy] == 0 and tem[xx][yy] == 1:
                    q.append((xx, yy))
                    bfs(xx, yy)    

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    tem = [[0] * m for _ in range(n)]
    ch = [[0] * m for _ in range(n)]
    count = 0
    
    for i in range(k):
        x, y = map(int, input().split())
        tem[y][x] = 1
        
    for j in range(n):
        for k in range(m):
            if ch[j][k] == 0 and tem[j][k] == 1:
                bfs(j, k)
                count += 1
    print(count)
    


# dfs 풀이
# import sys 
# sys.setrecursionlimit(10000) 
# def dfs(x, y):
    
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < m:
#             if ch[xx][yy] == 0 and tem[xx][yy] == 1:
#                 ch[xx][yy] = 1
#                 dfs(xx, yy)

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# t = int(input())

# for _ in range(t):
#     m, n, k = map(int, input().split())
#     tem = [[0] * m for _ in range(n)]
#     ch = [[0] * m for _ in range(n)]
#     count = 0
    
#     for i in range(k):
#         x, y = map(int, input().split())
#         tem[y][x] = 1

#     for j in range(n):
#         for k in range(m):
#             if ch[j][k] == 0 and tem[j][k] == 1:
#                 dfs(j, k)
#                 count += 1
#     print(count)