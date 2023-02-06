import heapq, sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

res = []
for x, y in arr:
    heapq.heappush(res, y)
    if len(res) > x:
        heapq.heappop(res)
        
print(sum(res))