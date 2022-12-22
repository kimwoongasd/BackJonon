from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = []
for _ in range(m):
    a = list(map(int, input()))
    arr.append(a)

ch = [[-1] * n for _ in range(m)]
dq = deque()
dq.append((0, 0))
ch[0][0] = 0
while dq:
    x, y = dq.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and ch[xx][yy] == -1:
            if arr[xx][yy] == 0:
                ch[xx][yy] = ch[x][y]
                # 왼쪽부터 추가해야 작은 값이 출력된다
                dq.appendleft((xx, yy))
                
            elif arr[xx][yy] == 1:
                ch[xx][yy] = ch[x][y] + 1
                dq.append((xx, yy))

print(ch[m-1][n-1])