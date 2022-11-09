import sys
import heapq
n = int(sys.stdin.readline().strip())

tem = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    
    if a == 0:
        if len(tem) == 0:
            print(0)
        else:
            print(heapq.heappop(tem))
    else:
        heapq.heappush(tem, a)