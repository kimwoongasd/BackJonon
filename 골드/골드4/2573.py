import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    global ch, count
    dq = deque()
    dq.append((a, b))
    ch[a][b] = 1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
                if arr[xx][yy] != 0:
                    dq.append((xx, yy))
                    ch[xx][yy] = 1
                elif arr[xx][yy] == 0:
                    count[x][y] += 1
    return 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

flag = False
time = 0

while True:
    ch = [[0] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and ch[i][j] == 0:
                res.append(bfs(i, j))
    
    for k in range(n):
        for h in range(m):
            arr[k][h] -= count[k][h]
            if arr[k][h] < 0:
                arr[k][h] = 0
    if len(res) == 0:
        break
         
    if len(res) >= 2:
        flag = True
        break
    time += 1
    
if flag:
    print(time)
else:
    print(0)

# 시간초과, 틀림
# def land_bfs(a, b):
#     global ch_island
#     ch_island[a][b] = 1
#     dq = deque()
#     dq.append((a, b))
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] != 0 and ch_island[xx][yy] == 0:
#                 dq.append((xx, yy))
#                 ch_island[xx][yy] = 1

# def bfs(a, b):
#     global time, arr
#     time += 1
#     dq = deque()
#     dq.append((a, b))
#     ch = [[0] * m for _ in range(n)]
#     ch[a][b] = 1
#     count = 0
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
#                 if arr[xx][yy] == 0:
#                     dq.append((xx, yy))
#                     ch[xx][yy] = 1
#                 else:
#                     if arr[xx][yy] - 1 >= 0:
#                         arr[xx][yy] -= 1
#                         count += 1
#                         ch[xx][yy] = 1
#     return count

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)

# time = 0

# while True:
#     cnt = bfs(0, 0)
#     if cnt == 0:
#         break
    
#     ch_island = [[0] * m for _ in range(n)]
#     island = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] != 0 and ch_island[i][j] == 0:
#                 land_bfs(i, j)
#                 island += 1
                       
#     if island >= 2:
#         print(time)
#         exit(0)
# print(0)