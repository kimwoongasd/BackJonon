import sys, heapq
input = sys.stdin.readline

# deque가 아니라 heapq으로 풀어야 했다
# sorted때문에 시간복작도가 커졌다
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    ch[b] += 1

hq = []
for i in range(1, n + 1):
    if ch[i] == 0:
        heapq.heappush(hq, i)
        
        
res = []
while hq:
    x = heapq.heappop(hq)
    res.append(x)
    for i in arr[x]:
        ch[i] -= 1
        if ch[i] == 0:
            heapq.heappush(hq, i)
    
print(*res)

# 시간 초과
# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [[] for _ in range(n + 1)]
# ch = [0] * (n + 1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[a].append(b)
#     ch[b] += 1

# dq = deque()
# for i in range(1, n + 1):
#     if ch[i] == 0:
#         dq.append(i)
        
# res = []
# while dq:
#     x = dq.popleft()
#     res.append(x)
#     for i in arr[x]:
#         ch[i] -= 1
#         if ch[i] == 0:
#             dq.append(i)
#     tem = sorted(dq)
#     dq = deque(tem)
    
# print(*res)