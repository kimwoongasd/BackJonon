import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x : x[0])

res = []
cnt = 0
for x in arr:
    a, b = x[0], x[1]
    while res and a >= res[0]:
        heapq.heappop(res)
    heapq.heappush(res, b)
    cnt = max(cnt, len(res))

print(cnt)