import sys
from collections import deque
sys.setrecursionlimit(10**6)

# bfs
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    else:
        arr = []
        ch = [[0] * w for _ in range(h)]
        for i in range(h):
            c = list(map(int, input().split()))
            arr.append(c)
        
        count = 0
        dq = deque()
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1 and ch[i][j] == 0:
                    dq.append((i, j))
                    ch[i][j] = 1
                    while dq:
                        x, y = dq.popleft()
                        for k in range(8):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0 <= xx < h and 0 <= yy < w and arr[xx][yy] == 1 and ch[xx][yy] == 0:
                                dq.append((xx, yy))
                                ch[xx][yy] = 1
                    count += 1
                    
        print(count)
        
# dfs
# def dfs(x, y):
#     ch[x][y] = 1

#     for i in range(8):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < h and 0 <= yy < w and arr[xx][yy] == 1 and ch[xx][yy] == 0:
#             dfs(xx, yy)

# dx = [0, 1, 0, -1, 1, 1, -1, -1]
# dy = [1, 0, -1, 0, 1, -1, -1, 1]

# while True:
#     w, h = map(int, input().split())
    
#     if w == 0 and h == 0:
#         break
    
#     else:
#         arr = []
#         ch = [[0] * w for _ in range(h)]
#         for i in range(h):
#             c = list(map(int, input().split()))
#             arr.append(c)
        
#         count = 0
#         for i in range(h):
#             for j in range(w):
#                 if arr[i][j] == 1 and ch[i][j] == 0:
#                     dfs(i, j)
#                     count += 1
                    
#         print(count)