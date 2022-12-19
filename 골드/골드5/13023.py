import sys
input = sys.stdin.readline

def dfs(L, s):
    global ch, res
    if res == 1:
        return
    
    if L == 4:
        res = 1
        return
    
    else:
        for x in arr[s]:
            if ch[x] == 0:
                ch[x] = 1
                dfs(L + 1, x)
                ch[x] = 0

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
ch = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
ch = [0] * n
res = 0
for i in range(n):
    if ch[i] == 0:
        ch[i] = 1
        dfs(0, i)
        ch[i] = 0
    if res == 1:
        break

if res == 1:
    print(1)
else:
    print(0)


# 시간초과
# def dfs(L, s):
#     global ch, res
#     if res == 1:
#         return
    
#     if L == 4:
#         res = 1
#         return
    
#     else:
#         for i in range(n):
#             if arr[s][i] and ch[i] == 0:
#                 ch[i] = 1
#                 dfs(L + 1, i)
#                 ch[i] = 0

# n, m = map(int, input().split())
# arr = [[0] * n for _ in range(n)]
# ch = [0] * n
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1
# res = 0
# for i in range(n):
#     if ch[i] == 0:
#         ch[i] = 1
#         dfs(0, i)
#         ch[i] = 0
#     if res == 1:
#         break

# if res == 1:
#     print(1)
# else:
#     print(0)