def dfs(x, y, L, t):
    global res, tem
    # 4 칸의 최대합이 작을 때는 제외
    if res > t + (4 - L) * tem:
        return
    
    if L == 4:
        res = max(res, t)
        
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 0:
                # ㅗ 모양을 하기 위해서 2부터 다시 시작한다.
                if L == 2:
                    ch[xx][yy] = 1
                    dfs(x, y, L + 1, t + arr[xx][yy])
                    ch[xx][yy] = 0

                # 그 외 모양들
                ch[xx][yy] = 1
                dfs(xx, yy, L + 1, t + arr[xx][yy])
                ch[xx][yy] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
tem = 0
for _ in range(n):
    a = list(map(int, input().split()))
    tem = max(tem, max(a))
    arr.append(a)

ch = [[0] * m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        ch[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        ch[i][j] = 0
        
print(res)