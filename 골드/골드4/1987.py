import sys
input = sys.stdin.readline

# python 시간초과 pyp3 통과
def dfs(x, y, t):
    global alpa, tem

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c:
            if alpa[ord(arr[xx][yy]) - 65] == 0 and ch[xx][yy] == 0:
                alpa[ord(arr[xx][yy]) - 65] = 1
                ch[x][y] = 1
                dfs(xx, yy, t + 1)
                alpa[ord(arr[xx][yy]) - 65] = 0
                ch[x][y] = 0
    
    if t > tem:
        tem = t        
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]             

r, c = map(int, input().split())
res = 0
arr = []

for _ in range(r):
    arr.append(list(map(str, input())))

ch = [[0] * c for _ in range(r)]
alpa = [0] * 26
tem = 0
alpa[ord(arr[0][0]) - 65] = 1
ch[0][0] = 1
dfs(0, 0, 1)
if tem > res:
    res = tem

print(res)