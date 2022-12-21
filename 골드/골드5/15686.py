# 함수를 쓴 풀이
# 좀 더 빠르다
from itertools import combinations

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
home = [] 
ck = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ck.append((i, j))
        elif arr[i][j] == 1:
            home.append((i, j))

res = 2147000000
for x in combinations(ck, m):
    total = 0
    for s, e in home:
        d = 2147000000
        for i in range(m):
            d = min(d, abs(s - x[i][0]) + abs(e - x[i][1]))
        total += d
    res = min(res, total)
print(res)

# def dfs(L, idx):
#     global home, ch, ck, res
#     if idx > len(ck):
#         return
    
#     if L == m:
#         total = 0
#         for x, y in home:
#             d = 2174000000
#             for i in range(len(ck)):
#                 if ch[i] == 1:
#                     d = min(d, abs(x - ck[i][0]) + abs(y - ck[i][1]))
#             total += d
#         res = min(res, total)
    
#     ch[idx] = 1
#     dfs(L + 1, idx + 1)
#     ch[idx] = 0
#     dfs(L, idx + 1)

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)
# home = [] 
# ck = []
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 2:
#             ck.append((i, j))
#         elif arr[i][j] == 1:
#             home.append((i, j))

# ch = [0] * (len(ck) + 1)
# res = 2174000000

# dfs(0, 0)
# print(res)