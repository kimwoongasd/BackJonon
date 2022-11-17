n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
ch = [[0] * m for _ in range(n)]
ch[0][0] = arr[0][0]
for i in range(1, n):
    ch[i][0] = ch[i - 1][0] + arr[i][0]

for i in range(1, m):
    ch[0][i] = ch[0][i - 1] + arr[0][i]
    
for i in range(1, n):
    for j in range(1, m):
        ch[i][j] = max(ch[i - 1][j - 1], ch[i - 1][j], ch[i][j - 1]) + arr[i][j]

print(ch[n - 1][m - 1])

# 시간초과
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(x, y, t):
#     global res
#     if x == n and y == m:
#         if t > res:
#             res = t
#     else:
#         if x + 1 <= n and y + 1 <= m:
#             dfs(x + 1, y, t + arr[x][y])
#             dfs(x + 1, y + 1, t + arr[x][y])
#             dfs(x, y + 1, t + arr[x][y])

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)

# res = 0
# dfs(0, 0, 0)
# print(res)