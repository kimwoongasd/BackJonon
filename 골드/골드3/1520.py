import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DP를 활용해야 시간초과가 발생하지 않는다
def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    
    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if ch[x][y] != -1:
        return ch[x][y]
    
    tem = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] < arr[x][y]:
            tem += dfs(xx, yy)
    
    ch[x][y] = tem
    return ch[x][y]


dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

m, n = map(int, input().split())
arr = []
for _ in range(m):
    a = list(map(int, input().split()))
    arr.append(a)

ch = [[-1] * n for _ in range(m)]
print(dfs(0, 0))


# 시간초과
# def dfs(x, y):
#     global res
#     if x == m - 1 and y == n - 1:
#         res += 1
#         return
        
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0 <= xx < m and 0 <= yy < n and ch[xx][yy] == 0 and arr[xx][yy] < arr[x][y]:
#             ch[xx][yy] = 1
#             dfs(xx, yy)
#             ch[xx][yy] = 0


# dx = [0, 1, -1, 0]
# dy = [1, 0, 0, -1]

# m, n = map(int, input().split())
# arr = []
# for _ in range(m):
#     a = list(map(int, input().split()))
#     arr.append(a)

# ch = [[0] * n for _ in range(m)]
# res = 0
# ch[0][0] = 1
# dfs(0, 0)
# print(res)