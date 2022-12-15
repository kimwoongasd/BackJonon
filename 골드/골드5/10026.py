import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, color):
    global ch
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and arr[xx][yy] == color:
            dfs(xx, yy, color)

def c_dfs(x, y, color):
    global ch_2
    ch_2[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch_2[xx][yy] == 0:
            if color == "B" and color == arr[xx][yy]:  
                c_dfs(xx, yy, color)
            elif (color == "R" or color =="G") and (arr[xx][yy] == "R" or arr[xx][yy] == "G"):
                c_dfs(xx, yy, color)
                
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = []
for _ in range(n):
    a = list(map(str, input()))
    arr.append(a)

ch = [[0] * n for _ in range(n)]
ch_2 = [[0] * n for _ in range(n)]
res_1 = 0
res_2 = 0
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            dfs(i, j, arr[i][j])
            res_1 += 1
        
        if ch_2[i][j] == 0:
            c_dfs(i, j, arr[i][j])
            res_2 += 1
print(f"{res_1} {res_2}")