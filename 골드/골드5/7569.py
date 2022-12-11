from collections import deque

def bfs():
    while dq:
        x, y, z = dq.popleft()
        for i in range(6):
            xx = x + dx[i]
            yy = y + dy[i]
            zz = z + dz[i]
            if 0 <= xx < h and 0 <= yy < m and 0 <= zz < n and ch[xx][yy][zz] == 0 and arr[xx][yy][zz] == 0:
                ch[xx][yy][zz] = 1
                arr[xx][yy][zz] = arr[x][y][z] + 1
                dq.append((xx, yy, zz))

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
n, m ,h = map(int, input().split())
arr = []
for _ in range(h):
    tem = []
    for _ in range(m):
        a = list(map(int, input().split()))
        tem.append(a)
    arr.append(tem)

ch = [[[0] * n for _ in range(m)] for _ in range(h)]
dq = deque()

for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1 and ch[i][j][k] == 0:
                dq.append((i, j, k))
                ch[i][j][k] = 1

bfs()
       
res = 0
for x in arr:
    for y in x:
        for z in y:
            if z == 0:
                print(-1)
                exit(0)
        res = max(max(y), res)

print(res - 1)
