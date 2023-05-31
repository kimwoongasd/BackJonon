def dfs(a, b, idx, s):
    global res
    if idx == k:
        if res < s:
            res = s
        return
    
    for x in range(a, n):
        for y in range(b if x == a else 0, m):
            if ch[x][y] == 0:
                flag = True
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if 0 <= xx < n and 0 <= yy < m and ch[xx][yy] == 1:
                        flag = False

                if flag:
                    ch[x][y] = 1
                    dfs(x, y, idx + 1, s + arr[x][y])
                    ch[x][y] = 0

n, m, k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ch = [[0] * m for _ in range(n)]
res = -2147000000
                        
dfs(0, 0, 0, 0)
print(res)
