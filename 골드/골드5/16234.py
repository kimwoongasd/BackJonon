from collections import deque

def bfs(x, y):
    dq = deque()
    tem = []
    dq.append((x, y))
    tem.append([x, y])
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0:
                if s <= abs(arr[x][y] - arr[xx][yy]) <= e:
                    ch[xx][yy] = 1
                    dq.append((xx, yy))
                    tem.append((xx, yy))
    return tem

n, s, e = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
            
count = 0
while True:
    flog = False
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                ch[i][j] = 1
                tem = bfs(i, j)
                if len(tem) > 1:
                    flog = True
                    # 연합을 이루는 각 칸의 인구수
                    num = sum(arr[x][y] for x, y in tem) // len(tem)
                    for x, y in tem:
                        arr[x][y] = num
    # 국경선이 열지 않았을 때
    if not flog:
        break
    count += 1
print(count)