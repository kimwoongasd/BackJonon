import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global res
    res += 1
    dq = deque()
    dq.append((x, y))
    ch = [[0] * m for _ in range(n)]
    ch[x][y] = 1
    while dq:
        a, b = dq.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
                if arr[xx][yy] == 0:
                    dq.append((xx, yy))
                    ch[xx][yy] = 1
                    
                elif arr[xx][yy] >= 1:
                    arr[xx][yy] += 1
                               

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

res = 0
while True:
    tem = bfs(0, 0)
    flag = 0
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                flag = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
                
    if flag == 0:
        print(res - 1)
        break