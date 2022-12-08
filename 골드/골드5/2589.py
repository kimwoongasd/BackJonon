# pyp3 통과
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    ch = [[0] * m for _ in range(n)]
    ch[x][y] = 1
    count = 0
    while dq:
        a, b = dq.popleft()
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0 and arr[xx][yy] == "L":
                ch[xx][yy] = ch[a][b] + 1
                dq.append((xx, yy))
                count = max(ch[xx][yy], count)
        
    return count - 1
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(str, input()))
    arr.append(a)
res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            res = max(res, bfs(i, j))
print(res)