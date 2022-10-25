import sys
from collections import deque

n = int(input())
d = deque()

for _ in range(n):
    tem = list(map(str, sys.stdin.readline().split()))
    
    if tem[0] == "push":
        d.append(tem[1])
    elif tem[0] == "pop":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif tem[0] == "size":
        print(len(d))
    elif tem[0] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif tem[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)