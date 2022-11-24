# bfs
from collections import deque

def bfs(x, y, h):
    dq = deque()
    dq.append((x, y))
    
    while dq:
        a, b = dq.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] > h and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                dq.append((xx, yy))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

res = 1
for h in range(1, 101):
    ch = [[0] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if h < arr[j][k] and ch[j][k] == 0:
                count += 1
                ch[j][k] = 1
                bfs(j, k, h)
    
    res = max(res, count)
    
    if count == 0:
        break
print(res)


# 시간 단축 코드 dfs
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y, h):
#     ch[x][y] = -1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and arr[xx][yy] > h:
#             dfs(xx, yy, h)
        

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# n = int(input())
# arr = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)
    
# res = 0
# for h in range(1, 101):
#     ch = [[0] * n for _ in range(n)]
#     count = 0
#     for j in range(n):
#         for k in range(n):
#             if h < arr[j][k] and ch[j][k] == 0:
#                 count += 1
#                 dfs(j, k, h)
    
#     res = max(res, count)
    
#     if count == 0:
#         break
# print(res)

# 높이 h 이하인 지역을 2차원 리스트 ch를 통해서 1로 바꿈
# dfs를 통해서 물에 잠기지 않은 지역 count
# 3중 for문을 쓰기 떄문에 시간이 오래 걸리고 물에 잠기지 않은 부분을 다시 새서 오래걸림
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y):
#     global count, ch
#     ch[x][y] = -1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0:
#             dfs(xx, yy)
        

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# n = int(input())
# arr = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)
    
# res = 1
# for h in range(1, 101):
#     ch = [[0] * n for _ in range(n)]
#     for j in range(n):
#         for k in range(n):
#             for i in range(4):
#                 x = j + dx[i]
#                 y = k + dy[i]
#                 if 0 <= x < n and 0 <= y < n and h >= arr[j][k]:
#                     ch[j][k] = 1
#     count = 0             
#     for a in range(n):
#         for b in range(n):
#             if ch[a][b] == 0:
#                 dfs(a, b)
#                 count += 1
#     if res < count:
#         res = count
    
#     if count == 0:
#         break
# print(res)