import sys
import heapq

n = int(sys.stdin.readline())

lt = []
rt = []

for i in range(n):
    m = int(input())
    
    if len(lt) == len(rt):
        heapq.heappush(lt, -m)
    
    else:
        heapq.heappush(rt, m)
        
    if rt and rt[0] < -lt[0]:
        max_value = heapq.heappop(lt)
        min_value = heapq.heappop(rt)
        
        heapq.heappush(lt, -min_value)
        heapq.heappush(rt, -max_value)
        
    print(-lt[0])