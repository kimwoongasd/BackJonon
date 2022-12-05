n, k = map(int, input().split())
ch = [[0] * 201 for _ in range(201)]

for i in range(201):
    ch[1][i] = 1
    ch[i][1] = i

for i in range(2, 201):
    for j in range(2, 201):
        ch[i][j] = ch[i - 1][j] + ch[i][j - 1]

print(ch[k][n] % 1000000000)

# 시간초과
# def dfs(L, t, s):
#     global count
#     if t > n:
#         return
#     if L == k:
#         if t == n:
#             count += 1
#     else:
#         for i in range(n - s, - 1, -1):
#             dfs(L + 1, t + i, i)

# n, k = map(int, input().split())
# count = 0
# for i in range((n + 1)):
#     dfs(1, i, i)
# print(count % 1000000000)