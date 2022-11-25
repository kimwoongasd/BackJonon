from collections import deque
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    while dq:
        a, b = dq.popleft()
        if a == p_x and b == p_y:
            print(arr[a][b])
            break
        for i in range(8):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < n and arr[xx][yy] == 0:
                arr[xx][yy] = arr[a][b] + 1
                dq.append((xx, yy))

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

t = int(input())

for _ in range(t):
    n = int(input())
    x, y = map(int, input().split()) # 말의 현재 위치
    p_x, p_y = map(int, input().split()) # 목적지
    arr = [[0] * n for _ in range(n)]
    
    bfs(x, y)