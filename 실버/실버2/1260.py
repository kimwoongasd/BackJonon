from collections import deque

def dfs(x):
    ch[x] = 1
    print(x, end=" ")
    
    for k in arr[x]:
        if ch[k] == 0:
            dfs(k)

def bfs(x):
    q = deque()
    q.append(x)
    
    while q:
        t = q.popleft()
        ch[t] = 1
        print(t, end=" ")
        
        for k in arr[t]:
            if ch[k] == 0:
                ch[k] = 1
                q.append(k)
            

n, m, v = map(int, input().split())
arr = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
for i in range(1, n + 1):
    arr[i].sort()

dfs(v)
ch = [0] * (n + 1)
print()
bfs(v)

# 시간 더 오래 걸림
# def dfs(x):
#     print(x, end=" ")
#     ch[x] = 1
    
#     for i in range(n):
#         if arr[x - 1][i] == 1 and ch[i + 1] == 0:
#             dfs(i + 1)

# def bfs(x):
#     q = deque()
#     q.append(v)
#     ch[v] = 1
#     while q:
#         t = q.popleft()
#         print(t, end=" ")
#         for i in range(n):
#             if arr[t - 1][i] == 1 and ch[i + 1] == 0:
#                 ch[i + 1] = 1
#                 q.append(i + 1)

# n, m, v = map(int, input().split())
# arr = [[0] * n for _ in range(n)]
# ch = [0] * (n + 1)
# res = [0] * n

# for i in range(m):
#     x, y = map(int, input().split())
#     arr[x - 1][y - 1] = 1
#     arr[y - 1][x - 1] = 1

# dfs(v)
# ch = [0] * (n + 1)
# bfs(v)