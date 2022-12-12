from collections import deque

def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
                arr[xx][yy] = arr[x][y] + 1
                dq.append((xx, yy))
            
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
for _ in range(m):
    a = list(map(int, input().split()))
    arr.append(a)
dq = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dq.append((i, j))
bfs()
res = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
    res = max(res, max(arr[i]))
print(res - 1)