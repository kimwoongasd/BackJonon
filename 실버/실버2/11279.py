import sys
import heapq

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    
    if a == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -a)