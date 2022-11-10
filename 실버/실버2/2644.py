# bfs
from collections import deque

def bfs(x):
    dq = deque()
    dq.append(x)
    
    while dq:
        tem = dq.popleft()
        for i in arr[tem]:
            if ch[i] == 0:
                ch[i] = ch[tem] + 1
                dq.append(i)

n = int(input())
t_1, t_2 = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
bfs(t_1)
    
if ch[t_2] == 0:
    print(-1)
else:
    print(ch[t_2])

# dfs
# def dfs(x): 
#     for i in tem[x]:
#         if ch[i] == 0:
#             ch[i] = ch[x] + 1
#             dfs(i)


# n = int(input())
# t_1, t_2 = map(int, input().split())
# m = int(input())
# tem = [[] for _ in range(n + 1)]
# ch = [0] * (n + 1)

# for i in range(m):
#     x, y = map(int, input().split())
#     tem[x].append(y)
#     tem[y].append(x)
    
# for x in tem:
#     x.sort()
    

# dfs(t_1)
# if ch[t_2] == 0:
#     print(-1)
# else:
#     print(ch[t_2])