import sys
from collections import deque
input = sys.stdin.readline

# pypy3 풀림
n = int(input())
dq = deque()
dq.append([n])
res = []
while dq:
    x = dq.popleft()
    tem = x[0]
    if tem == 1:
        res = x
        break
    
    if tem % 3 == 0:
        dq.append([tem // 3] + x)
    if tem % 2 == 0:
        dq.append([tem // 2] + x)
        
    dq.append([tem - 1] + x)
    

print(len(res) - 1)
print(*res[::-1])